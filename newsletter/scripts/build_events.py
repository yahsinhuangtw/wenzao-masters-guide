#!/usr/bin/env python3
"""Build newsletter/data/events.json.

Inputs
  ../event-map/data/events.json   Prototype 3 events (read from the Wenzao announcement list)
  CURATION (below)                topic tags, delivery language, EN/VI/JA titles and one-line summaries
  NEW_EVENTS (below)              events read by hand from the NTU and Academia Sinica pages
                                  that scripts/scrape.py saved under data/raw/

Fields that a source page does not state are null. Delivery language is marked
"stated", "inferred" (from the title or abstract language) or "unknown".
Vietnamese and Japanese text was written by Claude and has not been reviewed
by native speakers.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
P3 = ROOT.parent / "event-map" / "data" / "events.json"
OUT = ROOT / "data" / "events.json"
AS_OF = "2026-10-17"

TOPICS = {
    "ai": {"en": "AI, data & statistics", "vi": "AI, dữ liệu & thống kê", "ja": "AI・データ・統計"},
    "lang": {"en": "Language, humanities & arts", "vi": "Ngôn ngữ, nhân văn & nghệ thuật", "ja": "言語・人文・芸術"},
    "social": {"en": "Society, law & economics", "vi": "Xã hội, luật & kinh tế", "ja": "社会・法・経済"},
    "health": {"en": "Health & life sciences", "vi": "Sức khỏe & khoa học đời sống", "ja": "健康・生命科学"},
    "eng": {"en": "Engineering & technology", "vi": "Kỹ thuật & công nghệ", "ja": "工学・技術"},
    "edu": {"en": "Education & teaching", "vi": "Giáo dục & giảng dạy", "ja": "教育・教授法"},
    "env": {"en": "Environment & sustainability", "vi": "Môi trường & bền vững", "ja": "環境・サステナビリティ"},
    "biz": {"en": "Business & entrepreneurship", "vi": "Kinh doanh & khởi nghiệp", "ja": "ビジネス・起業"},
    "skills": {"en": "Research skills & ethics", "vi": "Kỹ năng nghiên cứu & đạo đức", "ja": "研究スキル・倫理"},
    "career": {"en": "Study abroad & careers", "vi": "Du học & nghề nghiệp", "ja": "留学・キャリア"},
}

KINDS = {
    "lecture": {"en": "Lecture", "vi": "Bài giảng", "ja": "講演"},
    "workshop": {"en": "Workshop", "vi": "Hội thảo thực hành", "ja": "ワークショップ"},
    "conference": {"en": "Conference", "vi": "Hội nghị", "ja": "学会・会議"},
    "forum": {"en": "Forum", "vi": "Diễn đàn", "ja": "フォーラム"},
    "seminar": {"en": "Seminar", "vi": "Seminar", "ja": "セミナー"},
    "course": {"en": "Course / training", "vi": "Khóa học / đào tạo", "ja": "講座・研修"},
    "launch": {"en": "Launch event", "vi": "Sự kiện ra mắt", "ja": "発表会"},
    "competition": {"en": "Competition", "vi": "Cuộc thi", "ja": "コンペ"},
    "info-session": {"en": "Info session", "vi": "Buổi giới thiệu", "ja": "説明会"},
    "public": {"en": "Public event", "vi": "Sự kiện công chúng", "ja": "公開イベント"},
}

# city_en -> (area, vi, ja)
CITIES = {
    "Taipei": ("taipei", "Đài Bắc", "台北"),
    "New Taipei": ("north", "Tân Bắc", "新北"),
    "Taoyuan": ("north", "Đào Viên", "桃園"),
    "Hsinchu": ("north", "Tân Trúc", "新竹"),
    "Taichung": ("south", "Đài Trung", "台中"),
    "Chiayi": ("south", "Gia Nghĩa", "嘉義"),
    "Tainan": ("south", "Đài Nam", "台南"),
    "Kaohsiung": ("south", "Cao Hùng", "高雄"),
    "Pingtung County": ("south", "Bình Đông", "屏東"),
}

# Prototype 3 events. Tuple:
# (topics, delivery language or None, vi title, ja title, en blurb, vi blurb, ja blurb[, en title override])
P3_CURATION = {
    "530800": (["career", "edu"], None,
        "Tọa đàm EU Park: Các trường đại học Đức và du học tại Đức", "EUパーク講演:ドイツの大学とドイツ留学",
        "Talk on German universities and studying in Germany, held on the Wenzao campus in Kaohsiung.",
        "Buổi nói chuyện về các trường đại học Đức và du học Đức, tổ chức tại khuôn viên Wenzao (Cao Hùng).",
        "ドイツの大学とドイツ留学についての講演。会場は高雄の文藻外語大学。"),
    "530984": (["lang", "edu"], None,
        "Hội thảo viết sử trường đại học lần thứ 3", "第3回大学史執筆ワークショップ",
        "Workshop hosted by the National Cheng Kung University Museum in Tainan. Hybrid format.",
        "Hội thảo do Bảo tàng Đại học Quốc lập Thành Công (Đài Nam) tổ chức, kết hợp trực tiếp và trực tuyến.",
        "台南の成功大学博物館が主催するワークショップ。対面とオンラインの併用。"),
    "530981": (["ai", "biz"], None,
        "Khóa học tiếp thị AI và video ngắn (khóa 1)", "AIマーケティング・ショート動画講座(第1期)",
        "Course held in a computer classroom in Tainan, run by a science-park industry–academia association.",
        "Khóa học tổ chức tại phòng máy tính ở Đài Nam, do hiệp hội công nghiệp–học thuật của khu khoa học tổ chức.",
        "台南のコンピューター教室で開かれる講座。科学園区の産学協会が主催。"),
    "530973": (["lang"], None,
        "Hội nghị quốc tế lần thứ 11 về diễn giải đương đại triết học và văn học Trung Hoa",
        "第11回 中国哲学・文学の現代的解釈 国際学会",
        "In-person international conference at National Taipei University (New Taipei).",
        "Hội nghị quốc tế trực tiếp tại Đại học Quốc lập Đài Bắc (Tân Bắc).",
        "国立台北大学(新北市)で開かれる対面形式の国際会議。",
        "11th International Conference on Contemporary Interpretation of Chinese Philosophy and Literature"),
    "530971": (["lang", "edu"], None,
        "Hội nghị giảng dạy tiếng Anh Liên Á 2026 (Đại học Soochow / ETA-ROC)",
        "2026年 汎アジア英語教育(ELT)会議(東吳大学/ETA-ROC)",
        "Two-day English-teaching conference in Taipei (13–14 Nov), at Soochow University and the Jiantan Youth Activity Center.",
        "Hội nghị hai ngày về giảng dạy tiếng Anh tại Đài Bắc (13–14/11), ở Đại học Soochow và Trung tâm Hoạt động Thanh niên Kiếm Đàm.",
        "台北で2日間行われる英語教育の会議(11月13〜14日)。会場は東吳大学と劍潭青年活動センター。",
        "2026 Pan-Asia ELT Conference (Soochow University / ETA-ROC)"),
    "530967": (["lang"], None,
        "Diễn đàn quốc tế Solid Tides (Dự án Bonbon Wave, Pier-2)", "Solid Tides 国際フォーラム(駁二ボンボン・ウェーブ計画)",
        "Forum at the Pier-2 Art Center in Kaohsiung, on two dates (24 Oct and 21 Nov).",
        "Diễn đàn tại Pier-2 Art Center (Cao Hùng), diễn ra hai ngày: 24/10 và 21/11.",
        "高雄の駁二芸術特区で2回開催(10月24日と11月21日)。",
        "Solid Tides International Forum (Pier-2 Bonbon Wave Project)"),
    "530965": (["health"], None,
        "Hội nghị quốc tế 2026 về Khoa học Y sinh tiên tiến", "2026年 先端生物医科学国際会議",
        "Biomedical conference at China Medical University in Taichung.",
        "Hội nghị y sinh tại Đại học Y Trung Quốc (Đài Trung).",
        "台中の中国医薬大学で開かれる生物医科学の国際会議。",
        "2026 International Conference on Advanced Biomedical Sciences"),
    "530958": (["edu"], None,
        "Hội nghị quốc tế 2027 về theo đuổi sự xuất sắc trong giáo dục đại học",
        "2027年 高等教育における卓越性の追求 国際会議",
        "Higher-education conference at Ming Chuan University's Taoyuan campus, in March 2027.",
        "Hội nghị về giáo dục đại học tại cơ sở Đào Viên của Đại học Minh Truyền, tháng 3/2027.",
        "2027年3月、銘傳大学桃園キャンパスで開かれる高等教育の会議。",
        "2027 International Conference on Pursuing Excellence in Higher Education"),
    "530954": (["edu", "social"], None,
        "Hội thảo thực hành giáo dục liên thế hệ 2026", "2026年 世代間教育実践シンポジウム",
        "In-person symposium at Chaoyang University of Technology in Taichung.",
        "Hội thảo trực tiếp tại Đại học Khoa học Kỹ thuật Triều Dương (Đài Trung).",
        "台中の朝陽科技大学での対面シンポジウム。"),
    "530951": (["env", "edu"], None,
        "Lễ ra mắt nền tảng giáo dục hiểu biết về biển TODA", "TODA 海洋リテラシー・プラットフォーム発表会",
        "Launch event by the National Academy of Marine Research, in Tainan.",
        "Sự kiện ra mắt do Viện Nghiên cứu Biển Quốc gia tổ chức tại Đài Nam.",
        "国家海洋研究院による発表イベント(台南)。",
        "TODA Marine Literacy Platform Launch"),
    "530948": (["edu"], None,
        "Hội nghị thường niên 2026 của Hiệp hội Giáo dục Đại cương", "2026年 一般教育学会 年次大会",
        "Annual meeting of the General Education Association, at Chung Shan Medical University in Taichung.",
        "Hội nghị thường niên của Hiệp hội Giáo dục Đại cương, tại Đại học Y khoa Trung Sơn (Đài Trung).",
        "一般教育学会の年次大会。会場は台中の中山医学大学。",
        "2026 General Education Society Annual Conference"),
    "530944": (["health", "eng"], None,
        "Cuộc thi thiết kế y tế thông minh 2026 (vòng chung kết)", "2026年 スマート医療デザインコンペ(決勝)",
        "Finals of a smart-medical design competition, hosted by National Central University's biomedical department.",
        "Vòng chung kết cuộc thi thiết kế y tế thông minh, do khoa Y sinh Đại học Quốc lập Trung Ương tổ chức.",
        "スマート医療デザインコンペの決勝。国立中央大学の生物医学科が主催。"),
    "530943": (["eng", "ai", "career"], None,
        "Buổi tuyển chọn chương trình nhân tài robot thông minh", "スマートロボット人材育成プログラム 選抜説明会",
        "Information and selection sessions for a smart-robotics talent program, run by ITRI for the National Science and Technology Council. Two dates, in Hsinchu and Taoyuan.",
        "Các buổi giới thiệu và tuyển chọn cho chương trình nhân tài robot thông minh, do ITRI thực hiện cho Hội đồng Khoa học và Công nghệ Quốc gia. Hai ngày: Tân Trúc và Đào Viên.",
        "スマートロボット人材育成プログラムの説明・選抜会。工業技術研究院(ITRI)が国家科学及技術委員会のために実施。新竹と桃園の2回。",
        "Smart Robotics Talent Program: Selection Sessions"),
    "530938": (["edu"], None,
        "Hội nghị quốc tế về định hình văn hóa giáo dục qua đối thoại", "対話による教育文化の再構築 国際会議",
        "International conference at National Taiwan Normal University in Taipei.",
        "Hội nghị quốc tế tại Đại học Sư phạm Quốc lập Đài Loan (Đài Bắc).",
        "台北の国立台湾師範大学で開かれる国際会議。",
        "International Conference on Reshaping Educational Culture through Dialogue"),
    "530930": (["health", "social"], None,
        "Hội nghị học thuật Thể thao và Giải trí 2026", "2026年 スポーツ・レジャー学術会議",
        "Academic conference at the National University of Tainan.",
        "Hội nghị học thuật tại Đại học Quốc lập Đài Nam.",
        "国立台南大学で開かれる学術会議。",
        "2026 Sports and Leisure Academic Conference"),
    "530924": (["edu", "ai"], None,
        "Hội nghị quốc tế: Tái định hình đào tạo giáo viên trong kỷ nguyên AI", "国際会議:AI時代の教員養成を再考する",
        "Organized by National Taiwan Normal University, held at National Chengchi University in Taipei in April 2027.",
        "Do Đại học Sư phạm Quốc lập Đài Loan tổ chức, diễn ra tại Đại học Quốc lập Chính Trị (Đài Bắc) vào tháng 4/2027.",
        "国立台湾師範大学の主催。2027年4月、台北の国立政治大学で開催。",
        "International Conference: Reimagining Teacher Education in the AI Era"),
    "530910": (["skills"], None,
        "Diễn đàn luận văn sau đại học toàn quốc 2027 (Đại học Providence)", "2027年 全国大学院生論文フォーラム(静宜大学)",
        "A national forum for graduate-level papers, hosted at Providence University in Taichung. The event date is not stated; only the deadline is.",
        "Diễn đàn toàn quốc về luận văn bậc sau đại học, tổ chức tại Đại học Providence (Đài Trung). Bài đăng không nêu ngày tổ chức, chỉ có hạn chót.",
        "大学院レベルの論文を扱う全国フォーラム(静宜大学・台中)。開催日は記載なしで、締切のみ記載。",
        "2027 National Graduate Paper Forum (Providence University)"),
    "530904": (["env"], None,
        "Diễn đàn quốc tế thanh niên về khí hậu Tân Bắc 2026", "新北2026 国際ユース気候フォーラム",
        "Youth climate forum hosted by the New Taipei City Government.",
        "Diễn đàn thanh niên về khí hậu do Chính quyền thành phố Tân Bắc tổ chức.",
        "新北市政府が主催する、若者向けの気候フォーラム。",
        "New Taipei 2026 International Youth Climate Forum"),
    "530901": (["ai"], None,
        "Hội nghị thường niên 2026 của Hội Phương pháp Thống kê Đài Loan", "2026年 台湾統計方法学会 年次大会",
        "Annual meeting of the Taiwan Statistical Methodology Society, at the Science Education Center of National Taiwan Normal University.",
        "Hội nghị thường niên của Hội Phương pháp Thống kê Đài Loan, tại Trung tâm Giáo dục Khoa học thuộc Đại học Sư phạm Quốc lập Đài Loan.",
        "台湾統計方法学会の年次大会。会場は国立台湾師範大学の科学教育センター。",
        "2026 Taiwan Statistical Methodology Society Annual Meeting"),
    "530942": (["ai", "skills"], None,
        "Hội thảo viết học thuật với AI và nộp bài báo tạp chí", "AIを使った学術論文執筆・投稿ワークショップ",
        "Workshop on using AI for academic writing and journal submission, at National Taipei University (Taipei).",
        "Hội thảo về dùng AI để viết học thuật và nộp bài báo, tại Đại học Quốc lập Đài Bắc (Đài Bắc).",
        "AIを使った学術論文の執筆と投稿に関するワークショップ(国立台北大学)。",
        "AI Academic Writing and Journal Submission Workshop"),
    "530898": (["lang", "edu"], None,
        "GEELT 2027: Hội nghị đầu tiên về giáo dục tiếng Anh đại cương", "GEELT 2027:第1回 一般英語教育会議",
        "First conference on general English education, at National Chiayi University's Language Center.",
        "Hội nghị đầu tiên về giáo dục tiếng Anh đại cương, tại Trung tâm Ngôn ngữ Đại học Quốc lập Gia Nghĩa.",
        "一般英語教育についての第1回会議。国立嘉義大学言語センターが主催。",
        "GEELT 2027: 1st Conference on General English Education"),
    "530896": (["social", "edu"], None,
        "Hội nghị quốc tế 2026 về năng lực đa văn hóa và tham vấn", "2026年 多文化コンピテンスとカウンセリング 国際会議",
        "International conference at National Pingtung University.",
        "Hội nghị quốc tế tại Đại học Quốc lập Bình Đông.",
        "国立屏東大学で開かれる国際会議。",
        "2026 International Conference on Multicultural Competence and Counseling"),
    "530893": (["health", "social"], None,
        "Bài giảng đặc biệt của Academia Sinica: Cải cách y tế toàn cầu và khả năng chống chịu kinh tế",
        "中央研究院 特別講演:世界の保健改革と経済のレジリエンス",
        "In-person special lecture at Academia Sinica's International Conference Hall in Nangang, Taipei.",
        "Bài giảng đặc biệt trực tiếp tại Hội trường Hội nghị Quốc tế của Academia Sinica (Nam Cảng, Đài Bắc).",
        "中央研究院(台北・南港)の国際会議ホールで行われる対面の特別講演。",
        "Academia Sinica Special Lecture: Reforming Global Health and Economic Resilience"),
    "530885": (["biz", "social"], None,
        "Hội nghị quốc tế 2026 về khả năng chống chịu và quản trị", "2026年 レジリエンスとマネジメント 国際会議",
        "Conference hosted by the Resilience Research Center at National Tsing Hua University in Hsinchu.",
        "Hội nghị do Trung tâm Nghiên cứu Khả năng Chống chịu của Đại học Quốc lập Thanh Hoa (Tân Trúc) tổ chức.",
        "新竹の国立清華大学レジリエンス研究センターが主催する会議。",
        "2026 International Conference on Resilience and Management"),
    "530884": (["lang"], None,
        "Bài giảng của kiến trúc sư di sản người Pháp Renzo Wieder", "フランスの文化遺産建築家 Renzo Wieder 氏の講演",
        "In-person lecture hosted by the Bureau of Cultural Heritage, Ministry of Culture, in Taichung.",
        "Bài giảng trực tiếp do Cục Di sản Văn hóa, Bộ Văn hóa tổ chức tại Đài Trung.",
        "文化部文化資産局が主催する対面の講演(台中)。",
        "Lecture by French Heritage Architect Renzo Wieder"),
    "530881": (["skills", "ai"], None,
        "Bài giảng: Góc nhìn của EU về đạo đức nghiên cứu trong kỷ nguyên AI", "講演:AI時代の研究倫理 — EUの視点",
        "In-person lecture on research ethics in the AI era. Organized by NYCU; the venue is at National Kaohsiung Normal University.",
        "Bài giảng trực tiếp về đạo đức nghiên cứu trong kỷ nguyên AI. Do NYCU tổ chức; địa điểm tại Đại học Sư phạm Quốc lập Cao Hùng.",
        "AI時代の研究倫理についての対面講演。主催は陽明交通大学、会場は国立高雄師範大学。",
        "Lecture: An EU View on Research Ethics in the AI Era"),
}

P3_ONLINE = {
    "530829": ("info-session", ["career"], "Ministry of Education",
        "Buổi chia sẻ nhân tài hải ngoại TaiwanGPS và giới thiệu du học", "TaiwanGPS 海外人材シェアリング&留学説明会",
        "Online session by the Ministry of Education about overseas talent and studying abroad (Google Meet).",
        "Buổi trực tuyến do Bộ Giáo dục tổ chức về nhân tài hải ngoại và du học (Google Meet).",
        "教育部によるオンライン説明会。海外人材と留学がテーマ(Google Meet)。",
        "TaiwanGPS Overseas Talent Sharing and Study-Abroad Briefing"),
    "530970": ("forum", ["edu", "ai"], "NTNU Overseas Chinese Student Preparatory Program",
        "Diễn đàn phát triển giáo dục thanh niên châu Á 2026: Giáo dục cho sinh viên Hoa kiều trong kỷ nguyên AI",
        "2026年 アジア青年教育発展フォーラム:AI時代の華僑留学生教育",
        "Online forum on education for overseas Chinese students in the AI era (Google Meet).",
        "Diễn đàn trực tuyến về giáo dục cho sinh viên Hoa kiều trong kỷ nguyên AI (Google Meet).",
        "AI時代の華僑留学生教育をテーマにしたオンラインフォーラム(Google Meet)。",
        "2026 Asian Youth Education Development Forum: Education for Overseas Chinese Students in the AI Era"),
    "530880": ("seminar", ["skills"], "National Yang Ming Chiao Tung University",
        "Hội thảo đạo đức bảo vệ người tham gia nghiên cứu 2026 (X)", "2026年 研究参加者保護 倫理セミナー(X)",
        "Online ethics seminar on protecting research participants (Cisco Webex).",
        "Hội thảo trực tuyến về đạo đức bảo vệ người tham gia nghiên cứu (Cisco Webex).",
        "研究参加者の保護に関するオンライン倫理セミナー(Cisco Webex)。",
        "2026 Research Participant Protection Ethics Seminar (X)"),
    "530918": ("workshop", ["skills", "career"], "Academia Sinica / EMBO",
        "Hội thảo đào tạo trực tuyến: Kiến thức cơ bản về giao tiếp", "コミュニケーション基礎 オンライン研修",
        "Online training workshop on communication fundamentals, on two dates.",
        "Hội thảo đào tạo trực tuyến về kiến thức giao tiếp cơ bản, hai ngày.",
        "コミュニケーションの基礎を学ぶオンライン研修(2日間)。",
        "Fundamentals of Communication Online Training Workshop"),
    "530912": ("course", ["skills"], "National Tsing Hua University",
        "Khóa đào tạo đạo đức nghiên cứu (trực tuyến)", "研究倫理研修(オンライン講座)",
        "Online research-ethics training course.",
        "Khóa đào tạo trực tuyến về đạo đức nghiên cứu.",
        "研究倫理のオンライン研修講座。",
        "Research Ethics Training (Online Course)"),
}

HSSB = "Humanities and Social Sciences Building (South Wing), Academia Sinica"
LING_LIST = "https://www.ling.sinica.edu.tw/main/en?act=activity_list&c=list&type=1"


def ev(id, source, kind, title_orig, en, vi, ja, org, topics, sessions, area, hub, url, blurb, lang=None,
       lang_basis="unknown", fmt=None, deadline=None, register_url=None, note=None):
    return {
        "id": id, "source": source, "kind": kind,
        "title": {"orig": title_orig, "en": en, "vi": vi, "ja": ja},
        "organizer_en": org, "topics": topics, "format": fmt, "sessions": sessions,
        "area": area, "hub": hub, "deadline": deadline,
        "language": {"value": lang, "basis": lang_basis},
        "blurb": blurb, "note": note, "url": url, "register_url": register_url,
    }


def sess(date, time=None, venue=None, city="Taipei", end=None):
    return {"date": date, "end_date": end, "time": time, "venue_en": venue, "city_en": city}


def trio(en, vi, ja):
    return {"en": en, "vi": vi, "ja": ja}


NEW_EVENTS = [
    ev("ntu-ethics-1023", "ntu", "lecture",
       "【學術倫理講座】運動科學研究與學術倫理的平衡羅盤",
       "Academic Ethics Lecture: Balancing Sports-Science Research and Research Ethics",
       "Tọa đàm đạo đức học thuật: Cân bằng giữa nghiên cứu khoa học thể thao và đạo đức nghiên cứu",
       "学術倫理講座:スポーツ科学研究と学術倫理のバランス",
       "NTU Center for General Education", ["skills", "health"],
       [sess("2026-10-23", "14:20-16:20", "Room R248, 2F, NTU Sports Center (main campus)")],
       "taipei", "ntu", "https://cge.ntu.edu.tw/News_Content_n_68407_s_266461.html",
       trio("Counts as 2 hours in category 4 of the academic-ethics requirement (master's and PhD students admitted from academic year 107, i.e. 2018, need at least 3 categories and 6 hours). No live stream; 50 seats.",
            "Tính là 2 giờ thuộc nhóm 4 của yêu cầu đạo đức học thuật (học viên thạc sĩ và tiến sĩ nhập học từ năm học 107, tức 2018, cần ít nhất 3 nhóm và 6 giờ). Không phát trực tuyến; 50 chỗ.",
            "学術倫理の必修要件のうち第4分類の2時間として認められる(民国107学年度=2018年度以降入学の修士・博士は3分類6時間以上が必要)。ライブ配信なし、定員50名。"),
       lang="zh", lang_basis="stated", fmt="in-person",
       register_url="https://my.ntu.edu.tw/actregister/sessionList.aspx?actID=20263700_15",
       note=trio("Registration runs through NTU's own activity system. The page does not say whether students from other schools may attend.",
                 "Đăng ký qua hệ thống hoạt động riêng của NTU. Trang không nói rõ sinh viên trường khác có được tham dự hay không.",
                 "申込みはNTU独自の活動登録システム経由。他大学の学生が参加できるかはページに記載なし。")),
    ev("ntu-elid-1027", "ntu", "conference",
       "ELiD 2026 內溶小體離子通道與疾病國際研討會",
       "ELiD 2026: International Symposium on Endolysosomal Ion Channels and Disease",
       "ELiD 2026: Hội thảo quốc tế về kênh ion nội-lysosome và bệnh tật",
       "ELiD 2026:エンドリソソームのイオンチャネルと疾患に関する国際シンポジウム",
       "National Taiwan University", ["health"],
       [sess("2026-10-27")], "taipei", "ntu",
       "https://www.mc.ntu.edu.tw/clsmb/News.action?q_type=-1&q_itemCode=12305",
       trio("Biomedical symposium listed on NTU's homepage. We could not open the event page, so venue, time and language are not confirmed.",
            "Hội thảo y sinh được đăng trên trang chủ NTU. Chúng tôi không mở được trang sự kiện nên địa điểm, giờ và ngôn ngữ chưa được xác nhận.",
            "NTUのトップページに掲載された生物医学のシンポジウム。イベントページを開けなかったため、会場・時間・言語は未確認。"),
       note=trio("Only the title and date come from NTU's homepage list.",
                 "Chỉ có tiêu đề và ngày lấy từ danh sách trên trang chủ NTU.",
                 "タイトルと日付のみNTUのトップページの一覧から取得。")),
    ev("ntu-press-1019", "ntu", "public",
       "臺大出版中心三十週年慶",
       "NTU Press 30th Anniversary: Panel on Thirty Years of Academic Publishing",
       "Kỷ niệm 30 năm Nhà xuất bản NTU: Tọa đàm 30 năm xuất bản học thuật",
       "台大出版センター30周年記念:学術出版30年を語る座談会",
       "NTU Press", ["lang", "skills"],
       [sess("2026-10-19", "14:00-15:30", "First Conference Hall, NTU Administration Building")],
       "taipei", "ntu", "https://press.ntu.edu.tw/tw/news/show.php?refer=news2026.09.14-1",
       trio("Panel with NTU professors on the past and future of academic publishing, followed by a tea reception.",
            "Tọa đàm với các giáo sư NTU về quá khứ và tương lai của xuất bản học thuật, sau đó là tiệc trà giao lưu.",
            "NTUの教授陣が学術出版の過去と未来を語る座談会。終了後に茶話会あり。"),
       fmt="in-person"),
    ev("ntu-awec-1211", "ntu", "lecture",
       "Al，請坐副駕：溝通、寫作與研究（115-1 寫作教學中心演講）",
       "AI, Please Sit in the Co-pilot Seat: Communication, Writing and Research (NTU Writing Center talk, 115-1 series)",
       "AI, hãy ngồi ghế phụ lái: Giao tiếp, viết và nghiên cứu (buổi nói chuyện của Trung tâm Viết NTU)",
       "AI は副操縦士席へ:コミュニケーション・ライティング・研究(台大ライティングセンター講演)",
       "NTU Writing Center", ["skills", "ai"],
       [sess("2026-12-11")], "taipei", "ntu",
       "https://awec.ntu.edu.tw/al%ef%bc%8c-%e8%ab%8b%e5%9d%90%e5%89%af%e9%a7%95%ef%bc%9a-%e6%ba%9d%e9%80%9a%e3%80%81%e5%af%ab%e4%bd%9c%e8%88%87%e7%a0%94%e7%a9%b6/",
       trio("Talk series of the NTU Writing Center for this term; its page lists talks on AI, literature reviews and academic writing. NTU's homepage gives 11 Dec as the date.",
            "Chuỗi bài nói chuyện của Trung tâm Viết NTU trong học kỳ này; trang liệt kê các buổi về AI, tổng quan tài liệu và viết học thuật. Trang chủ NTU ghi ngày 11/12.",
            "今学期の台大ライティングセンターの講演シリーズ。AI、文献レビュー、学術ライティングなどの回がある。日付はNTUのトップページでは12月11日。"),
       register_url="https://my.ntu.edu.tw/actregister/sessionList.aspx?actID=20261260_03",
       note=trio("Time and room are not given on the series page; check it before you go.",
                 "Trang chuỗi bài nói chuyện không nêu giờ và phòng; hãy kiểm tra trước khi đến.",
                 "シリーズのページに時間と教室の記載なし。参加前に確認を。")),
    ev("as-ieas-1027", "sinica", "seminar",
       "【Metrics/Empirical Seminar】Are Public School Teachers Overpaid? Regression Discontinuity Evidence from a Ranked Waitlist in Kenya",
       "Are Public School Teachers Overpaid? Regression Discontinuity Evidence from a Ranked Waitlist in Kenya",
       "Giáo viên trường công có được trả lương quá cao? Bằng chứng hồi quy gián đoạn từ danh sách chờ xếp hạng ở Kenya",
       "公立学校の教員は高給すぎるのか?ケニアの順位付き待機リストを用いた回帰不連続デザインの証拠",
       "Institute of Economics, Academia Sinica", ["social"],
       [sess("2026-10-27", "14:30", "Conference Room B110, Institute of Economics, Academia Sinica")],
       "nangang", "academia-sinica",
       "https://www.econ.sinica.edu.tw/4d49b1b1-d551-4956-84a5-6bbf392d8417/posts/8500",
       trio("Seminar by Prof. Tessa Bold (Stockholm University) on the civil-service wage premium of Kenyan teachers.",
            "Seminar do GS. Tessa Bold (Đại học Stockholm) trình bày về mức chênh lệch lương công chức của giáo viên Kenya.",
            "Tessa Bold教授(ストックホルム大学)が、ケニアの教員の公務員賃金プレミアムを論じるセミナー。"),
       lang="en", lang_basis="inferred"),
    ev("as-ieas-1029", "sinica", "seminar",
       "【Empirical Seminar】Scaling Care, Saving Lives: Evidence from an Iterative Trial in Uganda",
       "Scaling Care, Saving Lives: Evidence from an Iterative Trial in Uganda",
       "Mở rộng chăm sóc, cứu sống người bệnh: Bằng chứng từ thử nghiệm lặp tại Uganda",
       "ケアの拡大と命を救うこと:ウガンダの反復試験からの証拠",
       "Institute of Economics, Academia Sinica", ["social", "health"],
       [sess("2026-10-29", "14:30", "Conference Room B110, Institute of Economics, Academia Sinica")],
       "nangang", "academia-sinica",
       "https://www.econ.sinica.edu.tw/4d49b1b1-d551-4956-84a5-6bbf392d8417/posts/8501",
       trio("Seminar by Prof. Jakob Svensson (Stockholm University) on scaling up a community health worker program in Uganda.",
            "Seminar do GS. Jakob Svensson (Đại học Stockholm) về việc mở rộng chương trình nhân viên y tế cộng đồng ở Uganda.",
            "Jakob Svensson教授(ストックホルム大学)が、ウガンダの地域保健ワーカー事業の拡大について論じるセミナー。"),
       lang="en", lang_basis="inferred"),
    ev("as-ling-1019", "sinica", "lecture",
       "語料庫語言學與兒童語音發展研究",
       "Corpus Linguistics and Children's Speech Development",
       "Ngôn ngữ học ngữ liệu và sự phát triển giọng nói của trẻ em",
       "コーパス言語学と子どもの音声発達研究",
       "Institute of Linguistics, Academia Sinica", ["lang", "health"],
       [sess("2026-10-19", "10:00-12:00", "Room 519, " + HSSB)],
       "nangang", "academia-sinica", "https://www.ling.sinica.edu.tw/main/zh-tw?/sign/1019",
       trio("Talk by the institute's director on speech-development measures drawn from two corpora of Taiwan Mandarin child speech.",
            "Bài nói chuyện của viện trưởng về các chỉ số phát triển giọng nói rút ra từ hai kho ngữ liệu tiếng Hoa phổ thông của trẻ em Đài Loan.",
            "所長が、台湾華語の子どもの音声コーパス2つから得た音声発達の指標を紹介する講演。"),
       lang="zh", lang_basis="inferred"),
    ev("as-ling-1022", "sinica", "lecture",
       "Austro-Tai Cultural History: Implication from Kra-Dai and Austronesian lexical comparisons",
       "Austro-Tai Cultural History: Implications from Kra-Dai and Austronesian Lexical Comparisons",
       "Lịch sử văn hóa Austro-Tai: Hàm ý từ so sánh từ vựng Kra-Dai và Nam Đảo",
       "オーストロ・タイ文化史:クラ・ダイ語とオーストロネシア語の語彙比較からの示唆",
       "Institute of Linguistics, Academia Sinica", ["lang"],
       [sess("2026-10-22", "10:00-12:00", "Room 525, Institute of Linguistics, Academia Sinica")],
       "nangang", "academia-sinica", "https://www.ling.sinica.edu.tw/main/zh-tw?/sign/www.ling.sinica.edu.tw/austrotai",
       trio("Historical-linguistics talk on shared Kra-Dai and Austronesian vocabulary and what it says about early cultures.",
            "Bài nói chuyện về ngôn ngữ học lịch sử: từ vựng chung giữa Kra-Dai và Nam Đảo cho biết gì về các nền văn hóa sơ khai.",
            "クラ・ダイ語とオーストロネシア語に共通する語彙から初期の文化を探る、歴史言語学の講演。"),
       lang="en", lang_basis="inferred"),
    ev("as-ling-1110", "sinica", "conference",
       "ILAS–NINJAL Joint Conference on Semantics",
       "ILAS–NINJAL Joint Conference on Semantics",
       "Hội nghị chung ILAS–NINJAL về ngữ nghĩa học", "ILAS–NINJAL 意味論合同会議",
       "Institute of Linguistics, Academia Sinica", ["lang"],
       [sess("2026-11-10", None, "Room 519, " + HSSB)],
       "nangang", "academia-sinica", "https://www.ling.sinica.edu.tw/main/en?/sign/ILAS-NINJAL",
       trio("One-day semantics conference with Japan's NINJAL. Free, but seats are limited.",
            "Hội nghị ngữ nghĩa học một ngày cùng NINJAL (Nhật Bản). Miễn phí nhưng số chỗ có hạn.",
            "日本の国立国語研究所(NINJAL)との1日の意味論会議。参加無料、席数に限りあり。"),
       lang="en", lang_basis="inferred", deadline="2026-10-31",
       register_url="https://www.ling.sinica.edu.tw/main/en?/sign/ILAS-NINJAL"),
    ev("as-ling-1111", "sinica", "conference",
       "Language Learning and Understanding for AI Scientists and Linguists",
       "Language Learning and Understanding for AI Scientists and Linguists",
       "Học và hiểu ngôn ngữ dành cho nhà khoa học AI và nhà ngôn ngữ học",
       "AI研究者と言語学者のための言語学習・理解",
       "Institute of Linguistics, Academia Sinica, with NINJAL", ["ai", "lang"],
       [sess("2026-11-11", None, "Conference Room II, " + HSSB, end="2026-11-12")],
       "nangang", "academia-sinica", "https://www.ling.sinica.edu.tw/main/en?/sign/LLU2026",
       trio("Two-day meeting bringing AI researchers and linguists together, co-organized with Japan's NINJAL. Registration is open.",
            "Hội nghị hai ngày đưa các nhà nghiên cứu AI và nhà ngôn ngữ học lại với nhau, đồng tổ chức với NINJAL (Nhật Bản). Đang mở đăng ký.",
            "AI研究者と言語学者が集う2日間の会合。日本のNINJALとの共催。参加登録受付中。"),
       lang="en", lang_basis="inferred", register_url="https://www.ling.sinica.edu.tw/main/en?/sign/LLU2026"),
    ev("as-ling-1116", "sinica", "lecture",
       "Puyuma and language endangerment",
       "Puyuma and Language Endangerment", "Tiếng Puyuma và nguy cơ ngôn ngữ", "プユマ語と言語の危機",
       "Institute of Linguistics, Academia Sinica", ["lang"],
       [sess("2026-11-16", "14:00-16:00", "Meeting Room 520, Institute of Linguistics, Academia Sinica")],
       "nangang", "academia-sinica", LING_LIST,
       trio("Talk by Josiane Cauquelin on the Puyuma language, an Austronesian language of Taitung.",
            "Bài nói chuyện của Josiane Cauquelin về tiếng Puyuma, một ngôn ngữ Nam Đảo ở Đài Đông.",
            "Josiane Cauquelin氏による、台東のオーストロネシア語プユマ語についての講演。"),
       lang="en", lang_basis="inferred",
       note=trio("The institute's list links to its home page, not to this event, so the link above is the list.",
                 "Danh sách của viện dẫn về trang chủ chứ không về sự kiện này, nên liên kết trên là trang danh sách.",
                 "研究所の一覧のリンクがトップページに飛ぶため、上のリンクは一覧ページ。")),
    ev("as-ling-1119", "sinica", "lecture",
       "Language, change, and shamanism: Over four decades of linguistic documentation in Nanwang Puyuma",
       "Language, Change, and Shamanism: Over Four Decades of Linguistic Documentation in Nanwang Puyuma",
       "Ngôn ngữ, biến đổi và shaman giáo: Hơn bốn thập kỷ ghi chép ngôn ngữ Puyuma ở Nam Vương",
       "言語・変化・シャーマニズム:南王プユマ語の40年にわたる記録",
       "Institute of Linguistics, Academia Sinica", ["lang", "social"],
       [sess("2026-11-19", "10:00-12:00", "Meeting Room 519, Institute of Linguistics, Academia Sinica")],
       "nangang", "academia-sinica", LING_LIST,
       trio("Talk by Josiane Cauquelin, using a short film that spans nearly four decades in a Puyuma community in Taitung.",
            "Bài nói chuyện của Josiane Cauquelin, dựa trên một đoạn phim ngắn kéo dài gần bốn thập kỷ về một cộng đồng Puyuma ở Đài Đông.",
            "Josiane Cauquelin氏が、台東のプユマ族の集落を約40年にわたり撮影した短編映像をもとに語る講演。"),
       lang="en", lang_basis="inferred",
       note=trio("The institute's list links to its home page, not to this event, so the link above is the list.",
                 "Danh sách của viện dẫn về trang chủ chứ không về sự kiện này, nên liên kết trên là trang danh sách.",
                 "研究所の一覧のリンクがトップページに飛ぶため、上のリンクは一覧ページ。")),
    ev("as-ling-1203", "sinica", "lecture",
       "Perfect, already, and the case against iamitives",
       "Perfect, Already, and the Case against Iamitives",
       "Thể hoàn thành, “already” và luận cứ chống lại iamitive", "完了、already、そして iamitive 反対論",
       "Institute of Linguistics, Academia Sinica", ["lang"],
       [sess("2026-12-03", "10:00-12:00", "Meeting Room 519, Institute of Linguistics, Academia Sinica")],
       "nangang", "academia-sinica", LING_LIST,
       trio("Semantics talk by Jozina Vander Klok, based on the Javanese word wis.",
            "Bài nói chuyện về ngữ nghĩa học của Jozina Vander Klok, dựa trên từ wis trong tiếng Java.",
            "Jozina Vander Klok氏による意味論の講演。ジャワ語の wis を題材にする。"),
       lang="en", lang_basis="inferred",
       note=trio("The institute's list links to its home page, not to this event, so the link above is the list.",
                 "Danh sách của viện dẫn về trang chủ chứ không về sự kiện này, nên liên kết trên là trang danh sách.",
                 "研究所の一覧のリンクがトップページに飛ぶため、上のリンクは一覧ページ。")),
    ev("as-ling-1208", "sinica", "lecture",
       "Modality for cross-linguistic use",
       "Modality for Cross-Linguistic Use", "Tình thái cho nghiên cứu đa ngôn ngữ", "言語横断的な法性(モダリティ)研究のために",
       "Institute of Linguistics, Academia Sinica", ["lang"],
       [sess("2026-12-08", "10:00", "Meeting Room 519, Institute of Linguistics, Academia Sinica", end="2026-12-09")],
       "nangang", "academia-sinica", LING_LIST,
       trio("Two-day session (8–9 Dec) led by Jozina Vander Klok, listed under the institute's lectures.",
            "Buổi hai ngày (8–9/12) do Jozina Vander Klok dẫn dắt, được xếp trong mục bài giảng của viện.",
            "Jozina Vander Klok氏による2日間のセッション(12月8〜9日)。研究所の講演一覧に掲載。"),
       lang="en", lang_basis="inferred",
       note=trio("The institute's list links to its home page, not to this event, so the link above is the list.",
                 "Danh sách của viện dẫn về trang chủ chứ không về sự kiện này, nên liên kết trên là trang danh sách.",
                 "研究所の一覧のリンクがトップページに飛ぶため、上のリンクは一覧ページ。")),
    ev("as-ling-afla34", "sinica", "conference",
       "The 34th Annual Meeting of the Austronesian Formal Linguistics Association (AFLA-34)",
       "The 34th Annual Meeting of the Austronesian Formal Linguistics Association (AFLA-34)",
       "Hội nghị thường niên lần thứ 34 của Hiệp hội Ngôn ngữ học Hình thức Nam Đảo (AFLA-34)",
       "第34回オーストロネシア形式言語学会年次大会(AFLA-34)",
       "Institute of Linguistics, Academia Sinica", ["lang"],
       [sess("2027-06-23", None, "Conference Room II, " + HSSB, end="2027-06-25")],
       "nangang", "academia-sinica", "https://www.ling.sinica.edu.tw/main/en?/sign/AFLA34",
       trio("Annual meeting hosted at Academia Sinica in June 2027. Submissions are open; the abstract deadline is 15 Jan 2027.",
            "Hội nghị thường niên tổ chức tại Academia Sinica vào tháng 6/2027. Đang nhận bài; hạn nộp tóm tắt là 15/1/2027.",
            "2027年6月に中央研究院で開かれる年次大会。投稿受付中で、アブストラクト締切は2027年1月15日。"),
       lang="en", lang_basis="inferred", deadline="2027-01-15"),
]


def area_of(city_en, venue_en=""):
    if "Academia Sinica" in (venue_en or ""):
        return "nangang"
    return CITIES.get(city_en, ("south",))[0]


def main():
    p3 = json.loads(P3.read_text(encoding="utf8"))
    out = []
    for e in p3["events"]:
        c = P3_CURATION[e["id"]]
        topics, lang, vi, ja, b_en, b_vi, b_ja = c[:7]
        title_en = c[7] if len(c) > 7 else e["title_en"]
        sessions = [{"date": s["date"], "end_date": None, "time": s["time"], "venue_en": s["venue_en"],
                     "city_en": s["city_en"]} for s in e["sessions"]]
        s0 = e["sessions"][0]
        area = area_of(s0["city_en"], s0["venue_en"])
        out.append(ev(
            "wzu-" + e["id"], "wzu-list", e["kind"], e["title_zh"], title_en, vi, ja, e["organizer_en"], topics,
            sessions, area, "academia-sinica" if area == "nangang" else None,
            "https://a001.wzu.edu.tw/article/" + e["id"], trio(b_en, b_vi, b_ja),
            fmt=e["format"], deadline=e["deadline"]))
    for e in p3["online"]:
        kind, topics, org, vi, ja, b_en, b_vi, b_ja, title_en = P3_ONLINE[e["id"]]
        out.append(ev(
            "wzu-" + e["id"], "wzu-list", kind, e["title_zh"], title_en, vi, ja, org, topics,
            [{"date": d, "end_date": None, "time": None, "venue_en": e.get("note"), "city_en": None}
             for d in e["dates"]],
            "online", None, "https://a001.wzu.edu.tw/article/" + e["id"], trio(b_en, b_vi, b_ja), fmt="online"))
    out.extend(NEW_EVENTS)

    # keep upcoming only; date for sorting = first session on/after AS_OF
    keep = []
    for e in out:
        ds = [s for s in e["sessions"] if s["date"] and (s["end_date"] or s["date"]) >= AS_OF]
        if e["sessions"] and any(s["date"] for s in e["sessions"]) and not ds:
            continue  # all sessions are in the past
        if ds:
            e["sessions"] = ds
        keep.append(e)
    keep.sort(key=lambda e: (min((s["date"] for s in e["sessions"] if s["date"]), default=e["deadline"] or "9999")))
    data = {
        "as_of": AS_OF,
        "note": ("Prototype 4 dataset. 'wzu-list' events come from Prototype 3 (Wenzao announcement list, read "
                 "2026-10-15); 'ntu' and 'sinica' events were read from public NTU and Academia Sinica pages on "
                 "2026-10-17. Fields a page does not state are null. Topic tags and the Vietnamese and Japanese "
                 "text were written by Claude and are not independently verified."),
        "topics": TOPICS, "kinds": KINDS,
        "cities": {k: {"en": k, "vi": v[1], "ja": v[2]} for k, v in CITIES.items()},
        "events": keep,
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf8")
    from collections import Counter
    print(len(keep), "events;", Counter(e["source"] for e in keep), Counter(e["area"] for e in keep))


if __name__ == "__main__":
    main()
