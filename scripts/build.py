"""Generate the AI design catalogue and transparent GitHub rankings."""
from __future__ import annotations
import argparse,csv,io,json,re
from datetime import datetime
from pathlib import Path
from ranking import dt,age_days,score,tier,status,rank,table
ROOT=Path(__file__).resolve().parents[1]
CATEGORIES={
 'studios':'设计 Agent 与原型工作台',
 'canvas':'可编辑画布与矢量设计',
 'skills':'前端设计、动效与审查 Skills',
 'design_systems':'设计系统与 DESIGN.md',
 'bridges':'设计转代码与 MCP 桥接',
 'diagrams':'图解与视觉表达',
 'research':'论文、基准与数据集',
 'historical':'历史与归档项目',
}
SCOPES={'core':'核心候选','adjacent':'相邻基础设施','research':'研究/评测','historical':'历史参考','restricted':'受限许可'}
LICENSE_STATUS={'verified':'开放许可证已核验','custom':'复合/条件许可','source_available':'源码可见但非 OSI 开源','unverified':'许可待核验'}
def validate(projects,snapshot):
 assert snapshot['schema_version']==1;dt(snapshot['as_of']);repos=[p['repo'] for p in projects]
 assert len(repos)==len(set(x.lower() for x in repos));assert set(repos)==set(snapshot['repositories'])
 for p in projects:
  assert re.fullmatch(r'[\w.-]+/[\w.-]+',p['repo']);assert p['category'] in CATEGORIES and p['scope'] in SCOPES;assert p['description'] and p['boundary'] and p['evidence'];datetime.strptime(p['reviewed_at'],'%Y-%m-%d');assert re.fullmatch(r'[a-f0-9]{40}',p['evidence_commit']);assert p['license_review']['status'] in LICENSE_STATUS
  m=snapshot['repositories'][p['repo']];assert m['canonical_repo'].lower()==p['repo'].lower();assert all(type(m[k]) is int and m[k]>=0 for k in ['stars','forks','commits_30d','commits_90d']);assert m['commits_30d']<=m['commits_90d'];dt(m['last_commit_at'])
 assert {p['repo'] for p in projects if p['baseline']} == {
  'emilkowalski/skills', 'github/replica', 'cathrynlavery/diagram-design', 'nexu-io/open-design',
 }
 for p in projects:
  for e in p['evidence']:
   assert e['url'] == f"https://github.com/{p['repo']}/blob/{p['evidence_commit']}/{e['path']}#L{e['line']}"
  assert p['license_review']['label'] and p['license_review']['note']
def render(projects,snapshot):
 m=snapshot['repositories'];asof=snapshot['as_of'];reviewed=max(p['reviewed_at'] for p in projects);ordered=rank(projects,m,asof);base=sum(bool(p['baseline']) for p in projects)
 intro=(ROOT/'docs/readme-intro.md').read_text(encoding='utf-8').strip();readme=[intro,f'## 当前收录\n\n**{len(projects)} 个项目，其中 {base} 个为用户参考项目，{len(projects)-base} 个为扩展收录。** 功能核验：{reviewed}；指标快照：`{asof}`（UTC）。\n\n每个分类先按维护状态分层，再综合 star（40%）、90 天默认分支提交（35%）和最近提交（25%）排序。维护分不代表设计质量、模型能力、可访问性或生产成熟度。','## 活跃核心项目速览\n\n仅展示核心候选、开放许可证已核验且近 90 天有提交的项目；受限许可、研究基准和相邻工具不进入此表。']
 shortlist=[p for p in ordered if p['scope']=='core' and p['license_review']['status']=='verified' and tier(p,m[p['repo']],asof)==0]
 readme.append(table(['项目','定位','Stars','90天提交','最近提交 UTC','维护分'],[[f"[{p['name']}](https://github.com/{p['repo']})",p['description'],f"{m[p['repo']]['stars']:,}",f"{m[p['repo']]['commits_90d']:,}",m[p['repo']]['last_commit_at'][:10],f"{score(m[p['repo']],asof):.1f}"] for p in shortlist[:12]]));readme.append('## 分类目录\n\n`★用户参考` 表示用户直接提供的项目。每个仓库只进入一个主分类；项目详表记录依赖和限制。')
 readme.append(table(['分类','数量','维护排序靠前的项目'],[[label,len([p for p in ordered if p['category']==k]),'、'.join(p['name'] for p in [x for x in ordered if x['category']==k][:3])] for k,label in CATEGORIES.items()]))
 detail=['# 项目说明与证据\n\n每项定位来自固定提交的官方 README，未安装运行全部项目。指标刷新不会自动重审功能和许可证。\n']
 for k,label in CATEGORIES.items():
  group=[p for p in ordered if p['category']==k];readme.append('### '+label);rows=[]
  for p in group:
   x=m[p['repo']];lic=p['license_review'];tags=[]
   if p['baseline']:tags.append('★用户参考')
   if tier(p,x,asof)==3:tags.append('归档/历史')
   if lic['status']!='verified':tags.append('许可注意')
   suffix=(' · '+' · '.join(tags)) if tags else ''
   rows.append([f"[{p['name']}](https://github.com/{p['repo']}){suffix}",p['description'],f"{x['stars']:,}",f"{x['commits_90d']:,}",x['last_commit_at'][:10],f"{score(x,asof):.1f}",lic['label']])
   ev=' · '.join(f"[来源{i+1}]({e['url']})" for i,e in enumerate(p['evidence']));detail.extend([f"## [{p['name']}](https://github.com/{p['repo']})",p['description'],f"- 分类：{label}；{SCOPES[p['scope']]}。\n- 适用边界：{p['boundary']}\n- 维护状态：{status(p,x,asof)}；30 天提交 {x['commits_30d']} 次，90 天提交 {x['commits_90d']} 次。\n- 许可：[{lic['label']}]({lic['source']})；{LICENSE_STATUS[lic['status']]}。{lic['note']}\n- 功能核验：{p['reviewed_at']}；{ev}。"])
  readme.append(table(['项目','定位','Stars','90天提交','最近提交 UTC','维护分','许可'],rows))
 readme.extend([
  (ROOT/'docs/selection.md').read_text(encoding='utf-8').strip(),
  '## 数据与维护\n\n- [项目详表与固定版本证据](docs/projects.md)\n- [综合、Star、活跃度、最近提交排序](docs/rankings.md)\n- [论文与基准](docs/research.md)\n- [检索与收录决策](research/README.md)\n- [排序方法](docs/methodology.md)\n- [贡献指南](CONTRIBUTING.md)',
  '## 许可\n\n本目录原创整理与脚本采用 [MIT](LICENSE)。链接项目、托管服务、数据集、素材和字体遵循各自条款。部分维护脚本沿用 [视频合集](https://github.com/ZanePoe/awesome_ai_video_creation) 的 MIT 实现。',
 ])

 rankings=[f'# 排序视图\n\n快照：`{asof}`。这是 GitHub 维护元数据排序，不是设计质量排行榜。所有视图先按维护状态分层。']
 for mode,label in [('balanced','综合维护分'),('stars','Star 优先'),('activity','90 天提交优先'),('recent','最近默认分支提交优先')]:
  rows=[]
  for p in rank(projects,m,asof,mode):
   x=m[p['repo']];rows.append([f"[{p['name']}](https://github.com/{p['repo']})",CATEGORIES[p['category']],status(p,x,asof),x['stars'],x['commits_90d'],x['last_commit_at'][:10],score(x,asof)])
  rankings.extend(['## '+label,table(['项目','分类','维护层','Stars','90天提交','最近提交 UTC','维护分'],rows)])
 buf=io.StringIO(newline='');w=csv.writer(buf,lineterminator='\n');w.writerow(['repo','name','category','scope','baseline','license','license_status','stars','commits_30d','commits_90d','last_commit_at','maintenance_status','score','as_of'])
 for p in ordered:
  x=m[p['repo']];w.writerow([p['repo'],p['name'],p['category'],p['scope'],p['baseline'],p['license_review']['label'],p['license_review']['status'],x['stars'],x['commits_30d'],x['commits_90d'],x['last_commit_at'],status(p,x,asof),score(x,asof),asof])
 return {'README.md':'\n\n'.join(readme)+'\n','docs/projects.md':'\n\n'.join(detail)+'\n','docs/rankings.md':'\n\n'.join(rankings)+'\n','data/rankings.csv':buf.getvalue()}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--check',action='store_true');a=ap.parse_args();read=lambda p:json.loads((ROOT/p).read_text(encoding='utf-8'));projects,snapshot=read('data/projects.json'),read('data/metrics.json');validate(projects,snapshot);out=render(projects,snapshot)
 for name,content in out.items():
  path=ROOT/name
  if a.check:
   if not path.exists() or path.read_text(encoding='utf-8')!=content:raise SystemExit('Stale generated file: '+name)
  else:path.parent.mkdir(parents=True,exist_ok=True);path.write_text(content,encoding='utf-8')
 print(('Checked' if a.check else 'Generated'),len(out),'files;',len(projects),'projects')
if __name__=='__main__':main()
