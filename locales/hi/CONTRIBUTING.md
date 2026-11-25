# योगदान मार्गदर्िका

डिज़ाइन Agent, Agent Skills, डिज़ाइन एडिटर या शोध बेंचमार्क का योगदान स्वीकार्य है। कृपया canonical GitHub रिपॉज़िटरी, मुख्य उपयोग, लागू सीमा, फ़ंक्शन और लाइसेंस के मूल लिंक दें। केवल होस्टेड सेवा पर चलने वाले प्रोजेक्ट मुख्य संग्रह में नहीं आते; डॉक्युमेंटेशन, फ़ॉर्मैट और रेफ़रेंस इंडेक्स का रूप स्पष्ट रूप से चिह्नित करना आवश्यक है।

`data/projects.json` बदलें, README या आधिकारिक डॉक्युमेंटेशन के फ़िक्स किए गए commit के लिंक बने रहने दें; LICENSE, NOTICE तथा डेटा, फ़ॉन्ट और सामग्री के स्वतंत्र नियम जाँचें। जनरेटेड README या रैंकिंग तालिका सीधे एडिट न करें। नए प्रोजेक्ट में `baseline` को `false` रखें; पहले संस्करण के चार सीड प्रोजेक्ट अपरिवर्तित रहेंगे।

लोकल मशीन पर Python 3.12+ और प्रमाणीकृत GitHub CLI (या सेट किया गया `GH_TOKEN`) चाहिए।

```sh
python scripts/refresh_metrics.py
python scripts/build.py
python -m unittest discover -s tests -v
python scripts/build.py --check
```

## बहुभाषी फ़ाइलें

- `data/projects.json` चीनी में canonical समीक्षा डेटा है: तथ्य यहीं एक बार बदले जाते हैं।
- अन्य भाषाओं का पाठ `locales/<lang>/entries.json` (`description`, `boundary`, `license_label`, `license_note`; जिन प्रोजेक्ट का canonical नाम चीनी अक्षरों में है उनके लिए बिना-चीनी `name`) और `locales/<lang>/ui.json` से आता है; `zh` सीधे `data/projects.json` पर गिरता है, इसलिए `locales/zh/entries.json` नहीं है।
- नया प्रोजेक्ट जोड़ते समय या भूमिका, सीमा और लाइसेंस-निष्कर्ष बदलते समय उसी PR में en/es/hi/fr चारों locale पूरे करें, वरना `python scripts/build.py --check` और `python -m unittest discover -s tests -v` फेल होंगे।
- स्थैतिक दस्तावेज़: अंग्रेज़ी रूट की `docs/` और `CONTRIBUTING.md` में, अन्य भाषाएँ `locales/<lang>/` में उसी सापेक्ष पाथ पर। मिरर में सापेक्ष लिंक उस फ़ाइल की अपनी डायरेक्टरी से resolves होते हैं: `locales/<lang>/CONTRIBUTING.md` में रिपॉज़िटरी रूट की `data/`, `scripts/`, `research/`, `LICENSE` और `record/` फ़ाइलों की ओर `../../` लिखें; `docs/readme-intro.md` अपवाद है, क्योंकि वह README में जोड़ा जाता है और भाषा-रूट से resolves होता है।
- `record/` और `research/` रचना-समय का मूल पाठ रखते हैं; वे ऑडिट ट्रेल हैं और उनका मशीन अनुवाद नहीं किया जाता।
- जनरेटेड फ़ाइलें (`README.md`, `docs/projects.md`, `docs/rankings.md`, `data/rankings.csv` और हर भाषा-मिरर की उसी नाम की फ़ाइलें) हाथ से न बदलें, वे `python scripts/build.py` बनाता है।
