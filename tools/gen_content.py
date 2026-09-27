#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generates content/ JSON files and Android assets for EnglishMaster.
All content is original (own definitions, own example sentences)."""
import json, os, random

random.seed(42)
ROOT = "/workspace"
CONTENT = os.path.join(ROOT, "content")
ASSETS = os.path.join(ROOT, "android", "app", "src", "main", "assets", "content")

LEVELS = [
    {"id": 1, "courseId": 1, "name": "Starter", "description": "Alphabet, greetings and the very basics", "order": 0},
    {"id": 2, "courseId": 1, "name": "Beginner", "description": "Simple everyday sentences (A1)", "order": 1},
    {"id": 3, "courseId": 1, "name": "Elementary", "description": "Daily conversation (A2)", "order": 2},
    {"id": 4, "courseId": 1, "name": "Pre-Intermediate", "description": "Expanding your range (A2+/B1)", "order": 3},
    {"id": 5, "courseId": 1, "name": "Intermediate", "description": "Confident communication (B1)", "order": 4},
    {"id": 6, "courseId": 1, "name": "Upper-Intermediate", "description": "Nuance and fluency (B2)", "order": 5},
    {"id": 7, "courseId": 1, "name": "Advanced", "description": "Precision and style (C1)", "order": 6},
    {"id": 8, "courseId": 1, "name": "Expert", "description": "Near-native command (C2)", "order": 7},
]

UNITS = []
LESSONS = []
uid = 100
lid = 1000
for lv in LEVELS:
    for uo in range(1, 4):
        uid += 1
        UNITS.append({
            "id": uid, "levelId": lv["id"], "order": uo,
            "name": f"{lv['name']} Unit {uo}",
            "description": f"Unit {uo} of the {lv['name']} level",
            "requiredXp": (lv["order"] * 3 + uo - 1) * 100,
        })
        for lo, (lname, ltype) in enumerate([
            ("Vocabulary Building", "NORMAL"),
            ("Grammar Focus", "NORMAL"),
            ("Practice & Application", "NORMAL"),
            ("Review", "REVIEW"),
            ("Checkpoint", "TEST"),
        ], start=1):
            lid += 1
            LESSONS.append({
                "id": lid, "unitId": uid, "order": lo, "name": lname,
                "lessonType": ltype, "xpReward": 20 if ltype == "NORMAL" else (15 if ltype == "REVIEW" else 30),
            })

UNIT_BY_ID = {u["id"]: u for u in UNITS}
LEVEL_BY_ID = {l["id"]: l for l in LEVELS}

# word, meaning(ja), pos, ipa, difficulty(1-8), freq(1-5), example(en), example(ja), plural, past, pp, ing, synonyms, antonyms, related, tags
VOCAB_RAW = [
 ("apple", "りんご", "NOUN", "/ˈæp.əl/", 1, 5, "I eat an apple every morning.", "私は毎朝りんごを食べます。", "", "", "", "", "fruit", "", "tree, juice", "food,basic"),
 ("book", "本", "NOUN", "/bʊk/", 1, 5, "She reads a book before bed.", "彼女は寝る前に本を読みます。", "books", "", "", "", "", "", "reading,library", "objects"),
 ("cat", "猫", "NOUN", "/kæt/", 1, 5, "The cat sleeps on the sofa.", "猫はソファで寝ます。", "cats", "", "", "", "feline", "dog", "kitten", "animals,basic"),
 ("dog", "犬", "NOUN", "/dɒɡ/", 1, 5, "My dog likes to play outside.", "私の犬は外で遊ぶのが好きです。", "dogs", "", "", "", "canine", "cat", "puppy", "animals,basic"),
 ("house", "家", "NOUN", "/haʊs/", 1, 5, "They live in a small house.", "彼らは小さな家に住んでいます。", "houses", "", "", "", "", "", "home,garden", "places"),
 ("water", "水", "NOUN", "/ˈwɔː.tər/", 1, 5, "Please give me a glass of water.", "水をコップ一杯ください。", "", "", "", "", "", "", "drink,rain", "food,nature"),
 ("eat", "食べる", "VERB", "/iːt/", 1, 5, "We eat dinner at seven.", "私たちは7時に夕食を食べます。", "", "ate", "eaten", "eating", "consume", "starve", "food,eater", "food,verbs"),
 ("drink", "飲む", "VERB", "/drɪŋk/", 1, 5, "He drinks coffee every day.", "彼は毎日コーヒーを飲みます。", "", "drank", "drunk", "drinking", "sip", "", "beverage,water", "food,verbs"),
 ("go", "行く", "VERB", "/ɡəʊ/", 1, 5, "I go to school by bus.", "私はバスで学校へ行きます。", "", "went", "gone", "going", "", "come", "school,street", "verbs,irregular"),
 ("come", "来る", "VERB", "/kʌm/", 1, 5, "Come here, please.", "こちらへ来てください。", "", "came", "come", "coming", "", "go", "visitor", "verbs,irregular"),
 ("big", "大きい", "ADJECTIVE", "/bɪɡ/", 1, 5, "They have a big garden.", "彼らには広い庭があります。", "", "", "", "", "large,huge", "small", "bigger", "size,adj"),
 ("small", "小さい", "ADJECTIVE", "/smɔːl/", 1, 5, "This is a small gift for you.", "これはあなたへの小さな贈り物です。", "", "", "", "", "little", "big", "smaller", "size,adj"),
 ("good", "良い", "ADJECTIVE", "/ɡʊd/", 1, 5, "That is a good idea.", "それはいい考えですね。", "", "", "", "", "great,fine", "bad", "better", "quality,adj"),
 ("bad", "悪い", "ADJECTIVE", "/bæd/", 1, 5, "Smoking is bad for your health.", "喫煙は健康に悪いです。", "", "", "", "", "terrible", "good", "worse", "quality,adj"),
 ("happy", "嬉しい", "ADJECTIVE", "/ˈhæp.i/", 1, 5, "She looks very happy today.", "彼女は今日とても嬉しそうに見えます。", "", "", "", "", "glad,joyful", "sad", "happiness", "emotion,adj"),
 ("morning", "朝", "NOUN", "/ˈmɔː.nɪŋ/", 1, 5, "I wake up at six in the morning.", "私は朝6時に起きます。", "mornings", "", "", "", "", "", "evening,night", "time"),
 ("friend", "友達", "NOUN", "/frend/", 1, 5, "He is my best friend.", "彼は私の親友です。", "friends", "", "", "", "pal", "enemy", "friendly", "people"),
 ("time", "時間", "NOUN", "/taɪm/", 1, 5, "What time is it now?", "今何時ですか。", "times", "", "", "", "", "", "moment,clock", "abstract"),
 ("school", "学校", "NOUN", "/skuːl/", 1, 5, "The children walk to school.", "子供たちは歩いて学校へ行きます。", "schools", "", "", "", "", "", "teacher,classroom", "places,education"),
 ("one", "一", "NUMBER", "/wʌn/", 1, 5, "I have one brother.", "私は兄弟が一人います。", "", "", "", "", "", "", "", "numbers"),
 ("write", "書く", "VERB", "/raɪt/", 1, 5, "She writes in a journal nightly.", "彼女は毎晩日記を書きます。", "", "wrote", "written", "writing", "", "read", "writer,letter", "verbs,irregular"),
 ("speak", "話す", "VERB", "/spiːk/", 1, 5, "Can you speak slowly?", "ゆっくり話してもらえますか。", "", "spoke", "spoken", "speaking", "talk", "", "speaker", "verbs,irregular"),
 ("take", "取る", "VERB", "/teɪk/", 1, 5, "Please take these keys.", "これらの鍵を持ってください。", "", "took", "taken", "taking", "", "give", "taker", "verbs,irregular"),
 ("see", "見る", "VERB", "/siː/", 1, 5, "We see the mountains from here.", "ここから山が見えます。", "", "saw", "seen", "seeing", "look", "", "viewer", "verbs,irregular"),
 ("child", "子供", "NOUN", "/tʃaɪld/", 1, 4, "The children are playing outside.", "子供たちは外で遊んでいます。", "children", "", "", "", "", "kid", "parent", "family"),
 ("foot", "足", "NOUN", "/fʊt/", 1, 4, "My foot hurts after running.", "走った後で足が痛いです。", "feet", "", "", "", "", "", "shoe,leg", "body,irregular"),
 ("tooth", "歯", "NOUN", "/tuːθ/", 1, 4, "Brush your teeth before bed.", "寝る前に歯を磨きましょう。", "teeth", "", "", "", "", "", "dental,mouth", "body,irregular"),
 ("travel", "旅行する", "VERB", "/ˈtræv.əl/", 2, 4, "We travel abroad once a year.", "私たちは年に一度海外旅行をします。", "", "traveled", "traveled", "traveling", "journey", "", "traveler,trips", "daily,verbs"),
 ("weather", "天気", "NOUN", "/ˈweð.ər/", 2, 4, "The weather is nice today.", "今日はいい天気ですね。", "", "", "", "", "", "", "rainy,sunny", "nature"),
 ("buy", "買う", "VERB", "/baɪ/", 2, 5, "I want to buy a new phone.", "新しいスマホを買いたいです。", "", "bought", "bought", "buying", "purchase", "sell", "shopping,buyer", "commerce,irregular"),
 ("sell", "売る", "VERB", "/sel/", 2, 4, "They sell fresh vegetables.", "彼らは新鮮な野菜を売っています。", "", "sold", "sold", "selling", "offer", "buy", "sales", "commerce,irregular"),
 ("important", "重要な", "ADJECTIVE", "/ɪmˈpɔː.tənt/", 2, 5, "This is an important meeting.", "これは重要な会議です。", "", "", "", "", "significant", "trivial", "importance", "academic,adj"),
 ("different", "異なる", "ADJECTIVE", "/ˈdɪf.ər.ənt/", 2, 5, "The two cities are very different.", "その二つの都市はとても違います。", "", "", "", "", "distinct", "similar", "difference", "academic,adj"),
 ("decide", "決める", "VERB", "/dɪˈsaɪd/", 2, 4, "Let us decide together.", "一緒に決めましょう。", "", "decided", "decided", "deciding", "choose", "postpone", "decision", "verbs"),
 ("suggest", "提案する", "VERB", "/səˈdʒest/", 2, 4, "Can you suggest a good restaurant?", "いいレストランを提案してくれますか。", "", "suggested", "suggested", "suggesting", "propose", "", "suggestion", "verbs"),
 ("environment", "環境", "NOUN", "/ɪnˈvaɪ.rən.mənt/", 2, 4, "We must protect the environment.", "私たちは環境を守らなければなりません。", "environments", "", "", "", "", "", "pollution,eco", "academic"),
 ("knowledge", "知識", "NOUN", "/ˈnɒl.ɪdʒ/", 2, 4, "Reading increases your knowledge.", "読書は知識を増やします。", "", "", "", "", "", "", "knowledgeable,know", "academic"),
 ("achieve", "達成する", "VERB", "/əˈtʃiːv/", 2, 4, "She worked hard to achieve her goal.", "彼女は目標を達成するために努力しました。", "", "achieved", "achieved", "achieving", "accomplish", "fail", "achievement", "verbs,academic"),
 ("improve", "改善する", "VERB", "/ɪmˈpruːv/", 2, 4, "I want to improve my English.", "英語を上達させたいです。", "", "improved", "improved", "improving", "enhance", "worsen", "improvement", "verbs,academic"),
 ("however", "しかしながら", "ADVERB", "/haʊˈev.ər/", 2, 5, "It rained. However, we enjoyed the trip.", "雨でした。それでも旅行は楽しみました。", "", "", "", "", "but,nevertheless", "", "", "connectors"),
 ("because", "なぜなら", "CONJUNCTION", "/bɪˈkɒz/", 2, 5, "I stayed home because I was tired.", "疲れていた所以我は家にいました。", "", "", "", "", "", "", "so,reason", "connectors"),
 ("person", "人", "NOUN", "/ˈpɜː.sən/", 2, 5, "Each person received a badge.", "各人がバッジを受け取りました。", "people", "", "", "", "individual", "", "", "basic"),
 ("mouse", "マウス", "NOUN", "/maʊs/", 2, 3, "Click the mouse twice.", "マウスを二回クリックして。", "mice", "", "", "", "", "", "keyboard,computer", "tech,irregular"),
 ("goose", "ガチョウ", "NOUN", "/ɡuːs/", 2, 2, "The geese crossed the road.", "ガチョウたちが道を渡った。", "geese", "", "", "", "", "", "bird", "animals,irregular"),
 ("attitude", "態度・考え方", "NOUN", "/ˈæt.ɪ.tʃuːd/", 3, 4, "A positive attitude helps you learn faster.", "前向きな態度は学習を速めます。", "attitudes", "", "", "", "mindset", "", "", "academic"),
 ("behave", "振る舞う", "VERB", "/bɪˈheɪv/", 3, 3, "The children behaved very well.", "子供たちはとてもよく振る舞いました。", "", "behaved", "behaved", "behaving", "act", "", "behavior", "verbs"),
 ("rely", "頼る", "VERB", "/rɪˈlaɪ/", 3, 3, "You can rely on me.", "私を頼ってください。", "", "relied", "relied", "relying", "depend", "distrust", "reliable,on", "phrasals"),
 ("provide", "提供する", "VERB", "/prəˈvaɪd/", 3, 4, "The hotel provides free breakfast.", "そのホテルは無料の朝食を提供します。", "", "provided", "provided", "providing", "offer", "withhold", "provider,for", "verbs,academic"),
 ("develop", "発達させる", "VERB", "/dɪˈvel.əp/", 3, 4, "Cities develop very quickly.", "都市は非常に急速に発展します。", "", "developed", "developed", "developing", "grow", "", "development", "verbs,academic"),
 ("situation", "状況", "NOUN", "/ˌsɪtʃ.uˈeɪ.ʃən/", 3, 4, "It was a difficult situation.", "それは難しい状況でした。", "situations", "", "", "", "circumstance", "", "", "academic"),
 ("opportunity", "機会", "NOUN", "/ˌɒp.əˈtʃuː.nə.ti/", 3, 4, "This job is a great opportunity.", "この仕事は絶好の機会です。", "opportunities", "", "", "", "chance", "", "", "academic"),
 ("accurate", "正確な", "ADJECTIVE", "/ˈæk.jə.rət/", 3, 3, "The report must be accurate.", "報告は正確でなければなりません。", "", "", "", "", "precise", "inaccurate", "accuracy", "adj,academic"),
 ("gradually", "徐々に", "ADVERB", "/ˈɡrædʒ.u.ə.li/", 3, 3, "His English improved gradually.", "彼の英語は徐々に上達しました。", "", "", "", "", "slowly", "suddenly", "grade", "adverbs"),
 ("rather", "かなり・むしろ", "ADVERB", "/ˈrɑː.ðər/", 3, 4, "The exam was rather difficult.", "試験はかなり難しかった。", "", "", "", "", "quite", "", "", "adverbs"),
 ("look after", "世話を焼く", "PHRASAL_VERB", "/lʊk ˈɑːf.tər/", 3, 3, "She looks after her grandmother.", "彼女は祖母の世話をしています。", "", "looked after", "looked after", "looking after", "take care of", "neglect", "", "phrasals"),
 ("give up", "あきらめる", "PHRASAL_VERB", "/ɡɪv ˈʌp/", 3, 4, "Never give up your dream.", "夢をあきらめてはいけません。", "", "gave up", "given up", "giving up", "quit", "", "", "phrasals"),
 ("find out", "突き止める", "PHRASAL_VERB", "/faɪnd aʊt/", 3, 4, "I need to find out the truth.", "真実を突き止める必要があります。", "", "found out", "found out", "finding out", "discover", "", "", "phrasals"),
 ("turn down", "断る・音量を下げる", "PHRASAL_VERB", "/tɜːn daʊn/", 3, 3, "He turned down the offer.", "彼はその申し出を断りました。", "", "turned down", "turned down", "turning down", "reject", "accept", "", "phrasals"),
 ("certain", "特定の・確かな", "ADJECTIVE", "/ˈsɜː.tən/", 3, 4, "A certain person called you.", "ある人物があなたに電話をかけました。", "", "", "", "", "sure", "uncertain", "certainty", "adj"),
 ("analyze", "分析する", "VERB", "/ˈæn.ə.laɪz/", 4, 3, "Scientists analyze the data carefully.", "科学者はデータを注意深く分析します。", "", "analyzed", "analyzed", "analyzing", "examine", "", "analysis", "academic,tech"),
 ("approach", "アプローチする", "VERB", "/əˈprəʊtʃ/", 4, 4, "We should approach the problem differently.", "問題は別のやり方で扱うべきです。", "", "approached", "approached", "approaching", "", "", "approach", "academic"),
 ("assume", "仮定する", "VERB", "/əˈsuːm/", 4, 4, "Let us assume that the plan works.", "計画がうまくいくと仮定しましょう。", "", "assumed", "assumed", "assuming", "suppose", "", "assumption", "academic"),
 ("complicated", "複雑な", "ADJECTIVE", "/ˈkɒm.plɪ.keɪ.tɪd/", 4, 4, "The instructions were complicated.", "説明は複雑でした。", "", "", "", "", "complex", "simple", "complicate", "adj"),
 ("consequence", "結果", "NOUN", "/ˈkɒn.sɪ.kwəns/", 4, 4, "Every choice has consequences.", "すべての選択に結果が伴います。", "consequences", "", "", "", "result", "", "", "academic"),
 ("demonstrate", "実証する", "VERB", "/ˈdem.ən.streɪt/", 4, 4, "The study demonstrates a clear link.", "その研究は明確な関連を実証しています。", "", "demonstrated", "demonstrated", "demonstrating", "show", "", "demonstration", "academic"),
 ("efficient", "効率的な", "ADJECTIVE", "/ɪˈfɪʃ.ənt/", 4, 4, "This is a more efficient method.", "これはより効率的な方法です。", "", "", "", "", "effective", "inefficient", "efficiency", "business,adj"),
 ("motivate", "やる気にさせる", "VERB", "/ˈməʊ.tɪ.veɪt/", 4, 3, "Good teachers motivate their students.", "優れた教師は生徒のやる気を引き出します。", "", "motivated", "motivated", "motivating", "inspire", "discourage", "motivation", "verbs"),
 ("phenomenon", "現象", "NOUN", "/fəˈnɒm.ɪ.nən/", 4, 3, "Social media is a global phenomenon.", "SNSは世界的な現象です。", "phenomena", "", "", "", "", "", "", "academic"),
 ("significantly", "大幅に", "ADVERB", "/sɪɡˈnɪf.ɪ.kənt.li/", 4, 4, "Prices increased significantly.", "価格は大幅に上昇しました。", "", "", "", "", "considerably", "slightly", "significance", "adverbs,academic"),
 ("tendency", "傾向", "NOUN", "/ˈten.dən.si/", 4, 3, "He has a tendency to arrive late.", "彼は遅れて着く傾向がある。", "tendencies", "", "", "", "inclination", "", "", "academic"),
 ("acknowledge", "認める", "VERB", "/əkˈnɒl.ɪdʒ/", 4, 3, "Please acknowledge receipt of this email.", "このメールの受領を確認してください。", "", "acknowledged", "acknowledged", "acknowledging", "admit", "", "acknowledgement", "business"),
 ("ambiguous", "曖昧な", "ADJECTIVE", "/æmˈbɪɡ.ju.əs/", 4, 3, "His answer was ambiguous.", "彼の答えは曖昧でした。", "", "", "", "", "vague", "clear", "ambiguity", "adj,academic"),
 ("subsequently", "その後", "ADVERB", "/ˈsʌb.sɪ.kwənt.li/", 4, 3, "He subsequently became CEO.", "その後彼はCEOになりました。", "", "", "", "", "later", "", "", "connectors"),
 ("in spite of", "〜にもかかわらず", "EXPRESSION", "/ɪn spaɪt əv/", 4, 4, "In spite of the rain, the match continued.", "雨にもかかわらず試合は続いた。", "", "", "", "", "despite", "", "", "expressions"),
 ("advocate", "主張する", "VERB", "/ˈæd.və.keɪt/", 5, 3, "Many experts advocate a healthier diet.", "多くの専門家がより健康的な食事を主張しています。", "", "advocated", "advocated", "advocating", "recommend", "", "advocate", "academic"),
 ("coherent", "筋の通った", "ADJECTIVE", "/kəʊˈhɪə.rənt/", 5, 3, "She gave a coherent explanation.", "彼女は筋の通った説明をしました。", "", "", "", "", "logical", "incoherent", "coherence", "adj,academic"),
 ("controversial", "物議を醸す", "ADJECTIVE", "/ˌkɒn.trəˈvɜː.ʃəl/", 5, 3, "It remains a controversial policy.", "それは今も物議を醸す政策です。", "", "", "", "", "", "", "controversy", "adj,news"),
 ("implement", "実施する", "VERB", "/ˈɪm.plɪ.ment/", 5, 3, "The company implemented new rules.", "会社は新しい規則を実施した。", "", "implemented", "implemented", "implementing", "carry out", "", "implementation", "business"),
 ("inevitable", "避けられない", "ADJECTIVE", "/ɪnˈev.ɪ.tə.bəl/", 5, 3, "Change is inevitable.", "変化は避けられません。", "", "", "", "", "unavoidable", "avoidable", "inevitably", "adj,academic"),
 ("manipulate", "操る", "VERB", "/məˈnɪp.jə.leɪt/", 5, 3, "He tried to manipulate the results.", "彼は結果を操作しようとした。", "", "manipulated", "manipulated", "manipulating", "control", "", "manipulation", "verbs"),
 ("notion", "概念", "NOUN", "/ˈnəʊ.ʃən/", 5, 3, "I reject the notion that money buys happiness.", "お金が幸せを買うという概念は拒否します。", "notions", "", "", "", "concept", "", "", "academic"),
 ("perspective", "視点", "NOUN", "/pəˈspek.tɪv/", 5, 4, "Try to see it from my perspective.", "私の視点から見てみてください。", "perspectives", "", "", "", "viewpoint", "", "", "academic"),
 ("sophisticated", "洗練された", "ADJECTIVE", "/səˈfɪs.tɪ.keɪ.tɪd/", 5, 3, "This is a sophisticated system.", "これは洗練されたシステムです。", "", "", "", "", "advanced", "simple", "sophistication", "adj,tech"),
 ("thorough", "徹底した", "ADJECTIVE", "/ˈθʌr.ə/", 5, 3, "They did a thorough investigation.", "彼らは徹底した調査をした。", "", "", "", "", "complete", "superficial", "thoroughly", "adj"),
 ("undermine", "損なう", "VERB", "/ˌʌn.dəˈmaɪn/", 5, 3, "Constant criticism can undermine confidence.", "絶え間ない批判は自信を損なうことがある。", "", "undermined", "undermined", "undermining", "weaken", "strengthen", "", "verbs"),
 ("reluctant", "気が進まない", "ADJECTIVE", "/rɪˈlʌk.tənt/", 5, 3, "She was reluctant to speak publicly.", "彼女は公で話す気が進まなかった。", "", "", "", "", "unwilling", "eager", "reluctance", "adj"),
 ("at least", "少なくとも", "EXPRESSION", "/ət liːst/", 5, 5, "At least ten people attended.", "少なくとも10人が出席した。", "", "", "", "", "", "", "", "expressions"),
 ("as soon as", "〜するとすぐに", "EXPRESSION", "/æz suːn æz/", 5, 5, "Call me as soon as you arrive.", "到着したらすぐに電話して。", "", "", "", "", "", "", "", "expressions"),
 ("deteriorate", "悪化する", "VERB", "/dɪˈtɪə.ri.ə.reɪt/", 5, 3, "His health deteriorated rapidly.", "彼の健康は急速に悪化した。", "", "deteriorated", "deteriorated", "deteriorating", "worsen", "improve", "", "verbs,academic"),
 ("abolish", "廃止する", "VERB", "/əˈbɒl.ɪʃ/", 6, 2, "The government voted to abolish the tax.", "政府は投票でその税を廃止した。", "", "abolished", "abolished", "abolishing", "scrap", "establish", "abolition", "academic"),
 ("comprehensive", "包括的な", "ADJECTIVE", "/ˌkɒm.prɪˈhen.sɪv/", 6, 3, "We need a comprehensive review.", "包括的な見直しが必要です。", "", "", "", "", "thorough", "limited", "comprehensively", "business,adj"),
 ("dilemma", "ジレンマ", "NOUN", "/dɪˈlem.ə/", 6, 3, "She faced a moral dilemma.", "彼女は道徳的ジレンマに直面した。", "dilemmas", "", "", "", "", "", "", "academic"),
 ("eloquent", "雄弁な", "ADJECTIVE", "/ˈel.ə.kwənt/", 6, 2, "He gave an eloquent speech.", "彼は雄弁なスピーチをした。", "", "", "", "", "articulate", "inarticulate", "eloquence", "adj"),
 ("hypothesis", "仮説", "NOUN", "/haɪˈpɒθ.ə.sɪs/", 6, 3, "The experiment tested the hypothesis.", "実験は仮説を検証した。", "hypotheses", "", "", "", "", "", "theorize", "academic,science"),
 ("paradox", "逆説", "NOUN", "/ˈpær.ə.dɒks/", 6, 2, "It is a paradox that busy people find more time.", "忙しい人ほど時間を見つけるのは逆説的です。", "paradoxes", "", "", "", "", "", "paradoxical", "academic"),
 ("plausible", "もっともらしい", "ADJECTIVE", "/ˈplɔː.zə.bəl/", 6, 2, "That sounds like a plausible theory.", "それはもっともらしい理論に聞こえます。", "", "", "", "", "credible", "implausible", "plausibly", "adj,academic"),
 ("scrutiny", "精査", "NOUN", "/ˈskruː.tɪ.ni/", 6, 2, "The proposal came under close scrutiny.", "その提案は厳密な精査を受けた。", "", "", "", "", "", "", "scrutinize", "academic"),
 ("spurious", "偽りの", "ADJECTIVE", "/ˈspjʊə.ri.əs/", 6, 2, "They rejected the spurious claims.", "彼らは偽りの主張を一蹴した。", "", "", "", "", "false", "genuine", "", "adj,academic"),
 ("unprecedented", "前例のない", "ADJECTIVE", "/ʌnˈpres.ɪ.den.tɪd/", 6, 3, "Demand reached unprecedented levels.", "需要は前例のない水準に達した。", "", "", "", "", "", "", "precedent", "news,adj"),
 ("albeit", "虽然说…ではあるが", "EXPRESSION", "/ɔːlˈbiː.ɪt/", 6, 3, "The task was fun, albeit difficult.", "その課題は難しいながらも楽しかった。", "", "", "", "", "although", "", "", "formal,connectors"),
 ("thereby", "それによって", "ADVERB", "/ˌðeəˈraɪ/", 6, 3, "They cut costs thereby raising profits.", "彼らはコストを切り、それにより利益を高めた。", "", "", "", "", "", "", "", "formal,adverbs"),
 ("leverage", "活用する", "VERB", "/ˈliː.vər.ɪdʒ/", 6, 3, "Startups leverage social media wisely.", "スタートアップはSNSを賢く活用する。", "", "leveraged", "leveraged", "leveraging", "exploit", "", "", "business"),
 ("stakeholder", "利害関係者", "NOUN", "/ˈsteɪk.həʊl.dər/", 6, 3, "Consult every stakeholder first.", "まず全ての利害関係者に相談しなさい。", "stakeholders", "", "", "", "", "", "", "business"),
 ("mitigate", "軽減する", "VERB", "/ˈmɪt.ɪ.ɡeɪt/", 6, 3, "Planting trees can mitigate flooding.", "植林は洪水を軽減できる。", "", "mitigated", "mitigated", "mitigating", "lessen", "aggravate", "mitigation", "academic"),
 ("anachronism", "時代錯誤", "NOUN", "/əˈnæk.rə.nɪ.zəm/", 7, 1, "The law is an anachronism in modern society.", "その法律は現代社会では時代錯誤だ。", "anachronisms", "", "", "", "", "", "anachronistic", "academic,literary"),
 ("obfuscate", "分かりにくくする", "VERB", "/ˈɒb.fʌs.keɪt/", 7, 1, "Politicians sometimes obfuscate the issue.", "政治家はときどき問題をわざと曖昧にする。", "", "obfuscated", "obfuscated", "obfuscating", "confuse", "clarify", "obfuscation", "academic"),
 ("perfunctory", "形だけの", "ADJECTIVE", "/pəˈfʌŋk.tər.i/", 7, 1, "He gave a perfunctory nod.", "彼は形だけのうなずきを見せた。", "", "", "", "", "superficial", "", "", "literary,adj"),
 ("sycophant", "おべっか使い", "NOUN", "/ˈsɪk.ə.fænt/", 7, 1, "The boss ignored his sycophants.", "上司はおべっか使いたちを無視した。", "sycophants", "", "", "", "flatterer", "", "sycophantic", "literary"),
 ("verisimilitude", "真実らしさ", "NOUN", "/ˌveə.rɪ.sɪˈmɪl.ɪ.tʃuːd/", 7, 1, "The novel boasts remarkable verisimilitude.", "その小説は驚くべき真実らしさを誇る。", "", "", "", "", "", "", "verisimilar", "literary"),
 ("extemporize", "即興で行う", "VERB", "/ɪkˈstem.pər.aɪz/", 7, 1, "She can extemporize on any topic.", "彼女はどの話題でも即興で話せる。", "", "extemporized", "extemporized", "extemporizing", "improvise", "", "", "advanced,verbs"),
 ("pusillanimous", "臆病な", "ADJECTIVE", "/ˌpjuː.sɪˈlæn.ɪ.məs/", 8, 1, "A pusillanimous leader hesitated endlessly.", "臆病な指導者は際限なくためらった。", "", "", "", "", "cowardly", "bold", "", "literary,adj"),
 ("recalcitrant", "従わない", "ADJECTIVE", "/rɪˈkæl.sɪ.trənt/", 7, 1, "The recalcitrant child refused to apologize.", "言うことを聞かない子供は謝るのを拒んだ。", "", "", "", "", "defiant", "obedient", "", "literary,adj"),
 ("apocryphal", "出所不明の", "ADJECTIVE", "/əˈpɒk.rɪ.fəl/", 7, 1, "That quote is probably apocryphal.", "その引用はおそらく出所不明だ。", "", "", "", "", "dubious", "authentic", "", "academic,adj"),
 ("equanimity", "動じなさ", "NOUN", "/ˌek.wəˈnɪm.ɪ.ti/", 7, 1, "She kept her equanimity under pressure.", "彼女はプレッシャーの下でも動じなかった。", "", "", "", "", "composure", "agitation", "", "advanced,noun"),
]

EXPRESSIONS = [
 ("How is it going?","元気？どうしてる？","casual","Hi! How is it going?",1),
 ("Could you elaborate on that?","もう少し詳しく説明してもらえますか？","formal","Could you elaborate on that point, please?",4),
 ("I appreciate your help.","お手伝い感謝します。","polite","I really appreciate your help with this.",2),
 ("No worries.","気にしないで。","casual","A: Sorry I am late. B: No worries.",1),
 ("Would you mind opening the window?","窓を開けていただけますか？","polite","Would you mind opening the window a little?",3),
 ("Long time no see!","お久しぶりです！","idiom","Wow, long time no see!",1),
 ("It is up to you.","それはあなた次第です。","expression","Which movie shall we watch? It is up to you.",2),
 ("Hang in there.","頑張れ、負けるな。","encouragement","Exams are tough. Hang in there!",2),
 ("I am afraid I cannot make it.","申し訳ありませんが行けません。","business-formal","I am afraid I cannot make it to the meeting.",3),
 ("Please find attached the report.","レポートを添付いたします。","business","Please find attached the report for Q3.",4),
 ("Safe travels!","気をつけて！","travel","Bye! Safe travels!",1),
 ("Could I get the bill, please?","お会計をお願いできますか？","travel-dining","Excuse me, could I get the bill, please?",1),
 ("Where does this bus stop?","このバスはどこで停まりますか？","travel","Excuse me, where does this bus stop?",2),
 ("That makes sense.","なるほど、分かります。","conversation","Oh, that makes sense now.",2),
 ("Fair enough.","それでいいよ／まあ妥当だね。","conversation","We can meet at eight. Fair enough.",2),
 ("It rings a bell.","聞き覚えがあります。","idiom","The name rings a bell but I cannot place him.",3),
 ("Break a leg!","頑張って！（舞台）","idiom","You have a show tonight. Break a leg!",2),
 ("To be honest, I disagree.","正直に言うと反対です。","opinion","To be honest, I disagree with that plan.",3),
 ("With all due respect, ...","失礼ですが／敬意を表しつつも","formal-disagree","With all due respect, the data says otherwise.",5),
 ("Do you happen to know?","ひょっとしてご存知ですか？","indirect","Do you happen to know the train schedule?",3),
]

GRAMMAR = [
 ("Articles: a / an / the", 0, "Articles",
  "Use 'a' before consonant sounds and 'an' before vowel sounds. Use 'the' when both speakers know which specific thing is meant. Use no article for general plural or uncountable nouns.",
  "a + consonant sound | an + vowel sound | the + specific noun",
  ["I bought a book and an umbrella.|本と傘を一つずつ買いました。","The sun rises in the east.|太陽は東から昇ります。","Dogs are loyal animals.|犬は忠実な動物です。"],
  "'An university' is wrong because university starts with a /j/ sound. Say 'a university'.",
  "Countable and uncountable nouns|Prepositions", 1),
 ("Be verb: am / is / are", 0, "Verbs",
  "The verb 'be' links a subject to a description, identity, or location. It changes form with the subject and tense.",
  "Subject + am/is/are (+ complement)",
  ["She is a nurse.|彼女は看護師です。","We are ready now.|私たちもう準備できています。","They were late yesterday.|彼らは昨日遅れていました。"],
  "Do not add another main verb: 'He is like football' -> 'He likes football'.",
  "Present simple|Subject-verb agreement", 1),
 ("Present simple", 0, "Tenses",
  "Use the present simple for habits, facts, and general truths. Add -s or -es for he/she/it.",
  "Subject + verb(-s for third person)",
  ["I drink tea every morning.|毎朝紅茶を飲みます。","He works at a bank.|彼は銀行で働いています。","Water boils at 100 degrees.|水は100度で沸騰します。"],
  "Forgetting third-person -s: 'She go to school' -> 'She goes to school'.",
  "Present continuous|Adverbs of frequency", 1),
 ("Questions with do / does", 1, "Sentence types",
  "Form yes/no questions by putting do or does before the subject. Wh-questions add a question word at the front.",
  "Do/Does + subject + base verb? | Wh-word + do/does + subject + base verb?",
  ["Do you like jazz?|ジャズはお好きですか。","Does she live nearby?|彼女はこの近くに住んでいますか。","Where do you work?|どこでお仕事されていますか。"],
  "Keep only one marked verb: 'Does he likes it?' -> 'Does he like it?'.",
  "Present simple|Short answers", 1),
 ("Past simple", 1, "Tenses",
  "Use the past simple for finished actions. Regular verbs add -ed; irregular verbs change form and must be memorised.",
  "Subject + verb-ed / irregular past form",
  ["We visited Osaka last spring.|去年の春大阪を訪れました。","She bought a new laptop.|彼女は新しいノートパソコンを買った。","They did not agree at first.|最初は同意しなかった。"],
  "Double marking: 'Did you went?' -> 'Did you go?'.",
  "Irregular verbs|Past continuous", 2),
 ("Comparatives and superlatives", 2, "Comparison",
  "Use -er/more to compare two things and -est/most for three or more. Short adjectives take -er/-est; longer ones take more/most.",
  "adj-er + than | more + adj + than | the + adj-est | the most + adj",
  ["This box is heavier than that one.|この箱の方があの箱より重い。","It is the most interesting film I know.|知っている中で最も面白い映画です。"],
  "Do not stack markers: 'more bigger' -> 'bigger'.",
  "as...as|Adjectives", 2),
 ("Present perfect", 3, "Tenses",
  "Use have/has + past participle for past events with present relevance, life experience, or unfinished time periods.",
  "Subject + have/has + past participle",
  ["I have lived here for five years.|ここに住んで五年になります。","She has never eaten sushi.|彼女は食べたことがありません。","Have you finished yet?|もう終わりましたか。"],
  "Do not use finished time words: 'I have seen it yesterday' -> 'I saw it yesterday'.",
  "Past simple|for and since", 3),
 ("Future: will vs going to", 3, "Tenses",
  "Use will for instant decisions, promises and predictions. Use be going to for plans already made or evidence-based predictions.",
  "will + base verb | be going to + base verb",
  ["I will help you carry that.|それを持つのを手伝いますよ。","We are going to launch it in June.|6月に発売する予定です。","Look at those clouds - it is going to rain.|あの雲を見て、雨が降りそうだ。"],
  "'I will to call you' is wrong; will takes the bare infinitive: 'I will call you'.",
  "Present continuous for future|First conditional", 3),
 ("Passive voice", 4, "Voice",
  "Form the passive with be + past participle to focus on the action or when the agent is unknown or unimportant.",
  "Subject + be (any tense) + past participle (+ by agent)",
  ["The bridge was built in 1912.|この橋は1912年に建てられた。","Mistakes will be corrected.|間違いは訂正されます。","English is spoken worldwide.|英語は世界中で話されています。"],
  "Keep the correct form of be for each tense: 'was wrote' -> 'was written'.",
  "Past participles|Reporting agents with by", 4),
 ("Relative clauses", 4, "Clauses",
  "Use who for people, which for things, that for either, and where for places to add information without starting a new sentence.",
  "noun + who/which/that/where + clause",
  ["The teacher who explains clearly is popular.|わかりやすく説明する先生に人気があります。","This is the cafe that my sister recommended.|これは姉がお勧めしたカフェです。"],
  "Do not double the subject: 'The book which I read it' -> 'The book which I read'.",
  "Defining vs non-defining|Pronouns", 4),
 ("Conditionals (zero and first)", 4, "Mood",
  "Zero conditional states general results; first conditional states likely future results of a real condition. The if-clause uses present tense even about the future.",
  "if + present, present | if + present, will + base verb",
  ["If you heat ice, it melts.|氷を加熱すると溶けます。","If it rains tomorrow, we will stay in.|明日雨なら家にいます。"],
  "Never put will inside the if-clause: 'If it will rain' -> 'If it rains'.",
  "Second conditional|Unless", 4),
 ("Gerunds and infinitives", 5, "Verb patterns",
  "Some verbs take a gerund (-ing) and others take an infinitive (to + verb). The choice is fixed by the main verb and must be learned together.",
  "verb + doing | verb + to do",
  ["She enjoys reading novels.|彼女は小説を読むのを楽しみます。","They decided to move abroad.|彼らは海外に移ることに決めました。","Stop to smoke and stop smoking mean different things.|stop to smoke と stop smoking は意味が大きく変わります。"],
  "'I look forward to see you' is wrong; the to is a preposition: 'look forward to seeing you'.",
  "Preposition + gerund|Verb lists", 5),
 ("Reported speech", 5, "Speech",
  "When reporting what someone said, shift tenses back one step and adjust pronouns and time expressions.",
  "said/told + (that) + shifted clause",
  ["She said she was tired.|彼女は疲れたと言った。","He told me he would call later.|後で電話すると言われました。"],
  "Backshift consistently: 'He said he is busy yesterday' -> 'He said he had been busy'.",
  "Tense review|Question reporting", 5),
 ("Second and third conditionals", 5, "Mood",
  "Second conditional imagines unlikely present situations; third conditional regrets impossible past situations.",
  "if + past simple, would + base verb | if + past perfect, would have + past participle",
  ["If I had more time, I would learn piano.|時間がもっとあったならピアノを習うのに。","If she had studied, she would have passed.|勉強していたなら合格していたでしょう。"],
  "Match the halves: mixing second and third forms produces unclear meaning.",
  "Mixed conditionals|Wish", 6),
 ("Inversion after negative adverbials", 6, "Syntax",
  "When a negative or restrictive adverbial opens a sentence, invert subject and auxiliary for emphasis (formal style).",
  "Never/Rarely/Seldom/Hardly + auxiliary + subject + verb",
  ["Never have I seen such precision.|これほど精密なものを見たことがありません。","Not only did she win, but she also broke the record.|彼女は勝っただけでなく記録も更新した。"],
  "Keep normal order after mid-sentence adverbs: 'She never has...' is fine too.",
  "Emphasis clefts|Formal register", 7),
 ("Subjunctive mood", 7, "Mood",
  "Use the base form after verbs of demanding, suggesting, insisting, and in set phrases expressing wishes or hypotheticals.",
  "insist/demand/suggest + that + subject + base verb",
  ["I suggest that he study harder.|彼がもっと勉強すべきだと提案します。","If I were you, I would accept.|あなたの立場なら受け入れます。"],
  "Do not add -s in the that-clause in formal AmE: 'suggest that she study', not 'studies'.",
  "Wish clauses|Conditional review", 8),
]

READING = [
 (0, "A Day at the Park",
  "Anna goes to the park near her house every Sunday. She runs for twenty minutes and then sits under a big tree. Her brother brings sandwiches and orange juice. Birds come close because people often share their food. Anna feels calm before the busy week begins.",
  [("When does Anna visit the park?", ["Every Sunday","Every morning","On Saturdays","Once a month"], 0, "The first sentence says every Sunday."),
   ("What does her brother bring?", ["Sandwiches and juice","A ball","A newspaper","Cookies"], 0, "Her brother brings sandwiches and orange juice."),
   ("Why do birds come close?", ["Because people share food","Because of the tree","Because Anna sings","Because it rains"], 0, "The text links sharing food with the birds approaching.")],
  [("calm","落ち着いて"),("near","近くの"),("share","分かち合う")]),
 (1, "Learning to Cook",
  "When Ken moved into his first apartment, he could not cook anything. He watched short videos and practiced one dish each weekend. At first he burned rice and used too much salt. Six months later, friends asked him to host dinners. Ken learned that small, regular practice beats sudden effort.",
  [("How often did Ken practice?", ["Once a weekend","Every day","Twice a month","Never"], 0, "Ken practiced one dish each weekend."),
   ("What happened after six months?", ["Friends asked him to host dinners","He opened a restaurant","He moved out","He stopped cooking"], 0, "The text says friends asked him to host dinners."),
   ("What lesson does the passage teach?", ["Small regular practice beats sudden effort","Cooking is dangerous","Videos replace practice","Salt improves everything"], 0, "Final sentence states the moral.")],
  [("apartment","アパート"),("burned","焦がした"),("host","主催する")]),
 (2, "The Night Market",
  "Osaka's night markets glow with paper lanterns and the smell of grilled squid. Vendors shout prices while customers compare skewers. Tourists photograph everything, but locals simply eat and talk. A market lives longest when its regulars keep returning, not when its photos keep circulating.",
  [("What do vendors shout?", ["Prices","Directions","Poems","Weather reports"], 0, "Vendors shout prices."),
   ("What do tourists tend to do?", ["Photograph everything","Cook the squid","Clean the market","Sleep early"], 0, "Tourists photograph everything."),
   ("What keeps a market alive according to the author?", ["Returning regulars","Famous chefs","Government grants","TV programs"], 0, "Last sentence: regulars keep returning.")],
  [("vendors","行商人"),("skewers","串焼き"),("circulating","広まる")]),
 (3, "Remote Work Revolution",
  "Before 2020, commuting felt permanent. Then video calls replaced hallways, and kitchens became offices. Managers worried productivity would fall; several studies found it rose for focused tasks but fell for creative collaboration. The companies adapting best treat the office as a studio for teamwork, not a prison for attendance.",
  [("According to studies, remote productivity...", ["rose for focused tasks but fell for collaboration","always increased","always decreased","was unchanged"], 0, "The third sentence gives this contrast."),
   ("How do adaptive companies view the office?", ["A studio for teamwork","A place for punishment","An unnecessary expense","A training camp"], 0, "Final sentence: as a studio for teamwork.")],
  [("commuting","通勤"),("productivity","生産性"),("collaboration","協働")]),
 (4, "The Economics of Attention",
  "Every app competes for the same scarce resource: human attention. Designers measure scroll depth and pause length the way factories once measured output per hour. Critics call this behavioural surplus extraction; defenders argue users freely trade attention for free services. Either way, the business model shapes what we notice, and what we notice shapes what we value.",
  [("What do designers measure?", ["Scroll depth and pause length","Salary levels","Server costs","Battery size"], 0, "Second sentence."),
   ("What do critics call the practice?", ["Behavioural surplus extraction","Market failure","Public good","Creative destruction"], 0, "Third sentence names the critique."),
   ("What is the author's concluding claim?", ["Business models shape attention and thus values","Attention is unlimited","Apps should charge fees","Factories resemble apps"], 0, "The final sentence generalises.")],
  [("scarce","希少な"),("extraction","抽出"),("defenders","擁護者")]),
 (5, "On Translation Loss",
  "Translators joke that languages are polite conspiracies against directness. Japanese hedges with trailing verbs; Russian encodes aspect in the verb stem itself; English smuggles certainty into modal auxiliaries. A faithful translation therefore rarely reproduces words; it reconstructs intentions under foreign constraints, which is why two competent translators produce two defensible versions.",
  [("Japanese is described as...", ["hedging with trailing verbs","encoding aspect in stems","smuggling certainty","being overly literal"], 0, "Second sentence attributes hedging to Japanese."),
   ("Why do two translators differ?", ["Translation reconstructs intentions under constraints","One must be wrong","Words have single meanings","AI causes variation"], 0, "Final sentence explains defensibility of multiple versions.")],
  [("conspiracies","共謀"),("hedges","婉曲表現"),("auxiliaries","助動詞")]),
]

LISTENING_ITEMS = [
 ("She sells seashells by the sea.", "EARLY"),
 ("I would like a window seat, please.", "TRAVEL"),
 ("The meeting has been moved to Thursday.", "BUSINESS"),
 ("How much does it cost to repair the bike?", "EVERYDAY"),
 ("Turn left at the traffic lights.", "TRAVEL"),
 ("Could you repeat that more slowly?", "CLASSROOM"),
 ("He has been studying English for two years.", "GRAMMAR"),
 ("The train arrives at platform nine.", "TRAVEL"),
]

PLACEMENT_QUESTIONS = [
 ("Choose the correct sentence:", ["He don't like coffee.","He doesn't likes coffee.","He doesn't like coffee.","He not like coffee."], 2, 1),
 ("Fill in: Yesterday we ___ to the museum.", ["go","went","gone","going"], 1, 1),
 ("Fill in: This is the man ___ helped us.", ["which","who","whose","whom"], 1, 2),
 ("Choose the correct form:", ["I look forward to hear from you.","I look forward to hearing from you.","I look forward hear from you.","I looking forward to hearing you."], 1, 3),
 ("Fill in: If I ___ rich, I would travel the world.", ["am","will be","were","been"], 2, 4),
 ("Which sentence uses the passive correctly?", ["The letter was wrote yesterday.","The letter was written yesterday.","The letter wrote yesterday.","The letter is writing."], 1, 4),
 ("'Ubiquitous' is closest in meaning to:", ["rare","present everywhere","expensive","hidden"], 1, 6),
 ("Choose the inverted sentence:", ["Rarely I have seen that.","Rarely have I seen that.","I have rarely seen that that.","Have rarely I seen that."], 1, 7),
 ("Fill in: She insisted that he ___ the truth.", ["tells","tell","told","telling"], 1, 7),
 ("Which is grammatical?", ["Hardly had we arrived when it started.","Hardly we had arrived when it started.","We hardly had arrived when it started was.","Had hardly we arrived."], 0, 8),
]

ACHIEVEMENTS = [
 (1,"First Steps","Complete your first lesson","STAR","LESSONS_COMPLETED",1,20),
 (2,"Getting Serious","Complete 10 lessons","BOOK","LESSONS_COMPLETED",10,50),
 (3,"Scholar","Complete 50 lessons","GRADUATION_CAP","LESSONS_COMPLETED",50,200),
 (4,"Century","Earn 100 XP","MEDAL","TOTAL_XP",100,10),
 (5,"Half a Thousand","Earn 500 XP","MEDAL","TOTAL_XP",500,50),
 (6,"Thousandaire","Earn 1000 XP","TROPHY","TOTAL_XP",1000,100),
 (7,"Week Warrior","Keep a 7-day streak","FLAME","CURRENT_STREAK",7,50),
 (8,"Month Master","Keep a 30-day streak","FLAME","CURRENT_STREAK",30,200),
 (9,"Word Collector","Learn 100 words","WORD","WORDS_LEARNED",100,50),
 (10,"Wordsmith","Learn 500 words","WORD","WORDS_LEARNED",500,150),
 (11,"Lexicographer","Learn 1000 words","BOOK","WORDS_LEARNED",1000,300),
 (12,"Grammar Guru","Master 20 grammar topics","CHECK","GRAMMAR_MASTERED",20,100),
 (13,"Golden Ear","Complete 20 listening exercises","HEADPHONES","LISTENING_DONE",20,60),
 (14,"Bookworm","Complete 10 reading passages","BOOK","READING_DONE",10,60),
 (15,"Pen Pal","Complete 10 writing exercises","PEN","WRITING_DONE",10,60),
 (16,"Clear Voice","Complete 10 speaking exercises","MIC","SPEAKING_DONE",10,60),
 (17,"Perfect Round","Finish a lesson with no mistakes","TARGET","PERFECT_LESSONS",1,30),
 (18,"Flawless Five","Finish five lessons with no mistakes","TARGET","PERFECT_LESSONS",5,100),
]

XP_TABLE = {
    "exerciseCorrect": {"MULTIPLE_CHOICE":5,"TRUE_FALSE":3,"SPELLING":5,"FILL_IN_BLANK":6,"WORD_ORDERING":8,
                        "TRANSLATION":10,"LISTENING":7,"MATCHING":8,"READING":12,"WRITING":12,"SPEAKING":10,
                        "WORD_SELECTION":6,"SENTENCE_COMPLETION":7},
    "lessonBonus": {"NORMAL":20,"REVIEW":15,"TEST":30,"PRACTICE":10,"READING":20,"LISTENING":20,"SPEAKING":20,"WRITING":20},
    "perfectLessonBonus": 10,
    "checkpointBonus": 25,
}

def vocab_json():
    out = []
    for vid, row in enumerate(VOCAB_RAW, start=1):
        (word, meaning, pos, ipa, diff, freq, ex, exja, plural, past, pp, ing, syn, ant, rel, tags) = row
        out.append({
            "id": vid, "word": word, "meaning": meaning, "partOfSpeech": pos,
            "ipa": ipa, "difficulty": diff, "frequency": freq,
            "exampleSentence": ex, "exampleTranslation": exja,
            "synonyms": syn, "antonyms": ant, "relatedWords": rel,
            "plural": plural or None, "pastForm": past or None,
            "pastParticiple": pp or None, "presentParticiple": ing or None,
            "tags": [t for t in tags.split(",") if t],
        })
    return out

def grammar_json():
    out = []
    for gid, (title, lvl_order, cat, expl, struct, examples, mistakes, related, diff) in enumerate(GRAMMAR, start=1):
        out.append({
            "id": gid, "title": title, "levelOrder": lvl_order, "category": cat,
            "explanation": expl, "structure": struct,
            "examples": [{"text": e.split("|")[0], "translation": e.split("|")[1]} for e in examples],
            "commonMistakes": mistakes, "relatedGrammar": related, "difficulty": diff,
        })
    return out

def build_exercises_for_lesson(lesson, vocabs, grammar_items):
    rng = random.Random(lesson["id"])
    unit = UNIT_BY_ID[lesson["unitId"]]
    lv = LEVEL_BY_ID[unit["levelId"]]
    max_diff = lv["order"] + 2
    pool = [v for v in vocabs if v["difficulty"] <= max_diff] or vocabs
    gpool = [g for g in grammar_items if g["levelOrder"] <= lv["order"]] or [grammar_items[0]]
    exs = []
    eid = lesson["id"] * 100
    xpmap = XP_TABLE["exerciseCorrect"]
    def add(t, **kw):
        nonlocal eid
        eid += 1
        base = {"id": eid, "lessonId": lesson["id"], "order": len(exs) + 1,
                "exerciseType": t, "xpReward": kw.pop("xp", xpmap.get(t, 5)),
                "difficulty": kw.pop("diff", min(5, max_diff))}
        base.update(kw)
        exs.append(base)
    lt = lesson["lessonType"]
    picks = rng.sample(pool, min(6, len(pool)))

    def mc_meaning(v, instr="What does this word mean?"):
        wrongs = [p["meaning"] for p in pool if p["id"] != v["id"]]
        rng.shuffle(wrongs)
        opts = wrongs[:3] + [v["meaning"]]
        rng.shuffle(opts)
        add("MULTIPLE_CHOICE", question=v["word"], instruction=instr,
            options=opts, correctIndex=opts.index(v["meaning"]),
            explanation=f"{v['word']} {v['ipa']} : {v['meaning']}")

    if lt == "NORMAL" and "Vocabulary" in lesson["name"]:
        for v in picks[:4]:
            mc_meaning(v)
        for v in picks[:3]:
            masked = v["word"][0] + "*" * (len(v["word"]) - 1)
            add("SPELLING", question=f'{v["meaning"]} ({v["ipa"]})', instruction="Spell the English word",
                correctSpelling=v["word"], hint=masked)
        for v in picks[1:4]:
            others = [p["word"] for p in pool if p["id"] != v["id"]]
            rng.shuffle(others)
            opts = others[:3] + [v["word"]]
            rng.shuffle(opts)
            add("MULTIPLE_CHOICE", question=v["meaning"], instruction="Select the matching English word",
                options=opts, correctIndex=opts.index(v["word"]))
        for v in picks[:2]:
            if v["exampleSentence"]:
                words = [w.strip(".,?!") for w in v["exampleSentence"].split()]
                if 3 <= len(words) <= 9:
                    scr = words[:]
                    rng.shuffle(scr)
                    add("WORD_ORDERING", question=v["exampleTranslation"] or "Arrange the words",
                        instruction="Arrange the words into a sentence",
                        scrambledWords=scr, correctOrder=words)
    elif lt == "NORMAL" and "Grammar" in lesson["name"]:
        chosen = rng.sample(gpool, min(3, len(gpool)))
        for g in chosen:
            ex = g["examples"][0]["text"]
            add("TRUE_FALSE", question=f'{g["title"]}: "{ex}" follows this rule.',
                instruction="True or false?", isTrue=True, explanation=g["explanation"][:200])
        g = gpool[min(lv["order"], len(gpool) - 1)]
        ex = g["examples"][0]["text"]
        toks = ex.split()
        idx = min(2, len(toks) - 1)
        blanked = " ".join(["___" if i == idx else t for i, t in enumerate(toks)])
        add("FILL_IN_BLANK", question=blanked, instruction="Fill in the blank",
            correctAnswers=[toks[idx].strip(".,?!")], hint=g["structure"],
            explanation=g["explanation"][:200])
        for v in picks[:2]:
            if v["exampleSentence"]:
                words = [w.strip(".,?!") for w in v["exampleSentence"].split()]
                if 3 <= len(words) <= 9:
                    scr = words[:]
                    rng.shuffle(scr)
                    add("WORD_ORDERING", question=v["exampleTranslation"] or "Arrange the words",
                        instruction="Arrange the words into a sentence",
                        scrambledWords=scr, correctOrder=words)
    elif lt == "REVIEW":
        for v in picks[:3]:
            mc_meaning(v, instr="Review: what does this word mean?")
        pairs = [[v["word"], v["meaning"]] for v in picks[:4]]
        add("MATCHING", question="Match words with meanings", instruction="Match the pairs", pairs=pairs)
        item = LISTENING_ITEMS[lesson["id"] % len(LISTENING_ITEMS)]
        others = [x[0] for x in LISTENING_ITEMS if x[0] != item[0]]
        rng.shuffle(others)
        opts = others[:3] + [item[0]]
        rng.shuffle(opts)
        add("LISTENING", question="Listen and choose what you hear",
            instruction="Tap play, then select the sentence you hear",
            audioText=item[0], options=opts, correctIndex=opts.index(item[0]))
    elif lt == "TEST":
        for v in picks[:3]:
            mc_meaning(v, instr="Checkpoint: choose the meaning")
        for v in picks[:2]:
            add("TRANSLATION", question=v["meaning"], instruction="Translate into English",
                sourceLanguage="ja", targetLanguage="en",
                correctTranslations=([v["exampleSentence"].rstrip(".")] if v["exampleSentence"] else [v["word"]]),
                acceptableVariations=[v["word"]])
        item = LISTENING_ITEMS[lesson["id"] % len(LISTENING_ITEMS)]
        others = [x[0] for x in LISTENING_ITEMS if x[0] != item[0]]
        rng.shuffle(others)
        opts = others[:3] + [item[0]]
        rng.shuffle(opts)
        add("LISTENING", question="Listen and choose what you hear",
            instruction="Tap play, then select the sentence you hear",
            audioText=item[0], options=opts, correctIndex=opts.index(item[0]))
        rd = READING[lesson["id"] % len(READING)]
        q = rd[3][0]
        add("READING", question=rd[1], instruction="Read the passage and answer",
            passage=rd[2],
            readingQuestions=[{"question": q[0], "options": q[1], "correctIndex": q[2]}],
            vocabularyNotes=[{"word": w, "meaning": m} for (w, m) in rd[4]])
        tgt = picks[0]["exampleSentence"] or picks[0]["word"]
        add("SPEAKING", question=tgt, instruction="Say the sentence aloud", targetPhrase=tgt)
        add("WRITING", question=f'Write an English sentence using "{picks[1]["word"]}" ({picks[1]["meaning"]}).',
            instruction="Write a full English sentence",
            targetWord=picks[1]["word"], minWords=4)
    else:
        for v in picks[:4]:
            mc_meaning(v)
        pairs = [[v["word"], v["meaning"]] for v in picks[:4]]
        add("MATCHING", question="Match words with meanings", instruction="Match the pairs", pairs=pairs)
    return exs

def main():
    vocabs = vocab_json()
    grammars = grammar_json()
    exprs = [{"id": i, "expression": en, "meaning": ja, "tag": tag, "sample": sample, "difficulty": d}
             for i, (en, ja, tag, sample, d) in enumerate(EXPRESSIONS, start=1)]
    readings = [{"id": i, "levelOrder": lvl, "title": title, "text": text,
                 "questions": [{"question": q, "options": o, "correctIndex": c, "explanation": e} for (q, o, c, e) in qs],
                 "vocabularyNotes": [{"word": w, "meaning": m} for (w, m) in notes]}
                for i, (lvl, title, text, qs, notes) in enumerate(READING, start=1)]
    all_ex = []
    for lesson in LESSONS:
        all_ex.extend(build_exercises_for_lesson(lesson, vocabs, grammars))

    manifest = {"version": 1, "contentVersion": "1.1.0",
                "counts": {"levels": len(LEVELS), "units": len(UNITS), "lessons": len(LESSONS),
                           "vocabulary": len(vocabs), "grammar": len(grammars), "exercises": len(all_ex),
                           "reading": len(readings), "expressions": len(exprs),
                           "achievements": len(ACHIEVEMENTS)}}

    files = {
        "manifest.json": manifest,
        "levels.json": LEVELS,
        "units.json": UNITS,
        "lessons.json": LESSONS,
        "vocabulary/vocabulary.json": vocabs,
        "grammar/grammar.json": grammars,
        "expressions/expressions.json": exprs,
        "reading/reading.json": readings,
        "listening/listening.json": [{"id": i + 1, "text": t, "category": c} for i, (t, c) in enumerate(LISTENING_ITEMS)],
        "exercises/exercises.json": all_ex,
        "placement/placement_test.json": [{"id": i + 1, "question": q, "options": o, "correctIndex": c, "levelAward": la}
                                          for i, (q, o, c, la) in enumerate(PLACEMENT_QUESTIONS)],
        "achievements.json": [{"id": a, "name": n, "description": d, "icon": ic, "category": "GENERAL",
                               "requirementType": rt, "requirementValue": rv, "xpReward": xp}
                              for (a, n, d, ic, rt, rv, xp) in ACHIEVEMENTS],
        "config/xp_table.json": XP_TABLE,
    }

    for path, data in files.items():
        for base in (CONTENT, ASSETS):
            full = os.path.join(base, path)
            os.makedirs(os.path.dirname(full), exist_ok=True)
            with open(full, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=1)
    print("lessons:", len(LESSONS), "exercises:", len(all_ex), "vocab:", len(vocabs))

if __name__ == "__main__":
    main()
