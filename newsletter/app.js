(function () {
'use strict';

// ---------- UI strings (English, Vietnamese, Japanese) ----------
const T = {
  en: {
    skip: 'Skip to content', brand: 'Taiwan Campus Events Digest', back: 'Project page',
    pill: 'Prototype 4 · preview only, no email is sent',
    heroTitle: "Intellectual events across Taiwan, in your language and in your inbox.",
    heroLead: "Talks, workshops, conferences and public events from Taiwan's universities and Academia Sinica, picked for international master's students. Set your interests once and get a short digest in English, Tiếng Việt or 日本語.",
    pullEyebrow: 'Pull', pullTitle: 'Browse when you want',
    pullText: 'This page is the full list. Filter by topic, place and the language the event is given in, add one event to your calendar, or download your whole filtered list as a calendar file.',
    pushEyebrow: 'Push', pushTitle: 'Hear from us when it matters',
    pushText: 'The same filters become your newsletter: a weekly digest, plus a last-call reminder when a sign-up deadline is close. Use the tabs below to see exactly what each email would look like for your settings.',
    prefsTitle: 'Your newsletter',
    fInterests: 'Interests', fInterestsHint: 'Pick any. Leave empty to see everything.',
    fWhere: 'Where', fDeliv: 'Language of the event',
    fDelivHint: 'The newsletter is written in the language chosen at the top. This filter is about the language the event itself is given in.',
    delivAny: 'Any language', delivEn: 'English', delivZh: 'Chinese (Mandarin)',
    fUnknown: 'Also show events whose language is not stated',
    fPlan: 'What to send me',
    planWeekly: 'Weekly digest', planBoth: 'Weekly digest + last-call reminders', planLast: 'Last-call reminders only',
    fEmail: 'Email', fEmailHint: 'Demo only: nothing you type here is sent or stored.',
    subscribe: 'Subscribe (demo)', copyLink: 'Copy my settings link', copied: 'Link copied.', copyFail: 'Could not copy. Copy the address bar instead.', reset: 'Reset',
    subscribedMsg: 'Demo only. No email was sent and your address was not stored. Open the other tabs to see what you would receive.',
    needEmail: 'Enter an email address to try the sign-up. It is not sent anywhere.',
    tabBrowse: 'Browse events', tabDigest: 'Weekly digest', tabLast: 'Last-call reminder',
    count: (n, t) => `${n} of ${t} upcoming events match`,
    noMatch: 'No events match these settings. Try removing a filter or allowing events whose language is not stated.',
    icsAll: 'Download these as a calendar (.ics)', addCal: 'Add to calendar', source: 'Source page', register: 'Register / details',
    deadline: 'Deadline', dateTbc: 'Date not stated', timeNotStated: 'time not stated',
    langStated: l => l, langInferred: l => `${l} (inferred)`, langUnknown: 'Language not stated',
    fmtIn: 'In person', fmtOnline: 'Online', fmtHybrid: 'Hybrid',
    areas: { nangang: 'Nangang · Academia Sinica', taipei: 'Taipei (incl. NTU)', north: 'New Taipei, Taoyuan, Hsinchu', south: 'Central and southern Taiwan', online: 'Online' },
    langName: { en: 'English', zh: 'Chinese' },
    inPlan: 'Included in your settings: you would receive this email.',
    notInPlan: 'Not in your current settings: you would not receive this email.',
    mailFrom: 'From', mailTo: 'To', mailDate: 'Date',
    fromName: 'Taiwan Campus Events Digest',
    subjectWeekly: n => `${n} events for you in Taiwan`,
    subjectLast: n => `Last call: ${n} sign-up deadline${n === 1 ? '' : 's'} and events starting soon`,
    hello: 'Hello,',
    introWeekly: (n) => `Here are ${n} upcoming events that match your interests. Titles and summaries are in English; the original title follows each one.`,
    introLast: 'These sign-up deadlines are close, or the event starts within 3 days.',
    secNext7: 'In the next 7 days', secNext30: 'In the next 8 to 30 days', secLater: 'Later, or date not stated',
    secClosing: 'Sign-up closing in 14 days', secSoon: 'Starting within 3 days',
    nothing: 'Nothing in this section for your settings.',
    manage: 'Change your settings', unsub: 'Unsubscribe',
    mailFoot: 'You are receiving this because you chose these settings on the Taiwan Campus Events Digest prototype. In the real service the links below would use a one-click link that needs no password.',
    asOf: d => `Preview date: ${d}. The data was collected on this date, so the preview treats it as “today”.`,
    caveatTitle: 'Read this first',
    caveat: 'Early student prototype, not an official service. Event details were read from public pages on 15 and 17 October 2026 and not independently verified. Check the source page before you register or travel. Vietnamese and Japanese titles and summaries were written by an AI and have not been checked by native speakers; the original title is always shown.',
    notes: [
      'No email is sent. The preview shows what the digest would look like; the address you type is neither sent nor stored.',
      'Sources: the Wenzao announcement list (Prototype 3 data), National Taiwan University pages, and Academia Sinica institute pages (Economics, Linguistics). Not every department or institute is covered yet.',
      'Topic tags and language-of-event labels are our curation. “Inferred” means we guessed from the language of the title or abstract.',
      'Venue names are left in English. Some events are limited to members of the host school; the page says so only where the source did.',
      'Your settings are kept in the link of this page (the part after #) and in your browser only.'
    ],
    footText: 'Part of the campus AI contest project “Wenzao master’s guide”. Student pilot; not affiliated with the universities listed.'
  },
  vi: {
    skip: 'Chuyển đến nội dung', brand: 'Bản tin sự kiện học thuật Đài Loan', back: 'Trang dự án',
    pill: 'Nguyên mẫu 4 · chỉ xem thử, không gửi email',
    heroTitle: 'Sự kiện học thuật khắp Đài Loan, bằng ngôn ngữ của bạn, ngay trong hộp thư.',
    heroLead: 'Bài giảng, hội thảo, hội nghị và sự kiện công chúng từ các trường đại học Đài Loan và Academia Sinica, chọn lọc cho sinh viên thạc sĩ quốc tế. Chọn sở thích một lần và nhận bản tin ngắn bằng English, Tiếng Việt hoặc 日本語.',
    pullEyebrow: 'Tự tìm', pullTitle: 'Xem khi bạn muốn',
    pullText: 'Trang này là danh sách đầy đủ. Lọc theo chủ đề, địa điểm và ngôn ngữ của sự kiện, thêm từng sự kiện vào lịch, hoặc tải cả danh sách đã lọc về dưới dạng tệp lịch.',
    pushEyebrow: 'Gửi đến', pushTitle: 'Nhận tin khi cần thiết',
    pushText: 'Chính các bộ lọc đó trở thành bản tin của bạn: bản tin hằng tuần, cộng với nhắc nhở cuối cùng khi sắp hết hạn đăng ký. Dùng các thẻ bên dưới để xem chính xác từng email sẽ trông thế nào với thiết lập của bạn.',
    prefsTitle: 'Bản tin của bạn',
    fInterests: 'Sở thích', fInterestsHint: 'Chọn tùy ý. Để trống để xem tất cả.',
    fWhere: 'Địa điểm', fDeliv: 'Ngôn ngữ của sự kiện',
    fDelivHint: 'Bản tin được viết bằng ngôn ngữ chọn ở trên cùng. Bộ lọc này nói về ngôn ngữ mà chính sự kiện sử dụng.',
    delivAny: 'Bất kỳ ngôn ngữ nào', delivEn: 'Tiếng Anh', delivZh: 'Tiếng Trung (phổ thông)',
    fUnknown: 'Hiển thị cả sự kiện không nêu ngôn ngữ',
    fPlan: 'Tôi muốn nhận',
    planWeekly: 'Bản tin hằng tuần', planBoth: 'Bản tin hằng tuần + nhắc nhở cuối cùng', planLast: 'Chỉ nhắc nhở cuối cùng',
    fEmail: 'Email', fEmailHint: 'Chỉ là bản thử: những gì bạn nhập ở đây không được gửi đi hay lưu lại.',
    subscribe: 'Đăng ký (bản thử)', copyLink: 'Sao chép liên kết thiết lập', copied: 'Đã sao chép liên kết.', copyFail: 'Không sao chép được. Hãy sao chép từ thanh địa chỉ.', reset: 'Đặt lại',
    subscribedMsg: 'Chỉ là bản thử. Không có email nào được gửi và địa chỉ của bạn không được lưu. Mở các thẻ khác để xem bạn sẽ nhận được gì.',
    needEmail: 'Nhập một địa chỉ email để thử đăng ký. Địa chỉ này không được gửi đi đâu cả.',
    tabBrowse: 'Duyệt sự kiện', tabDigest: 'Bản tin hằng tuần', tabLast: 'Nhắc nhở cuối cùng',
    count: (n, t) => `${n} trong ${t} sự kiện sắp tới phù hợp`,
    noMatch: 'Không có sự kiện nào phù hợp. Hãy bỏ bớt bộ lọc hoặc cho phép hiển thị sự kiện không nêu ngôn ngữ.',
    icsAll: 'Tải danh sách này về lịch (.ics)', addCal: 'Thêm vào lịch', source: 'Trang nguồn', register: 'Đăng ký / chi tiết',
    deadline: 'Hạn chót', dateTbc: 'Chưa nêu ngày', timeNotStated: 'chưa nêu giờ',
    langStated: l => l, langInferred: l => `${l} (suy đoán)`, langUnknown: 'Chưa nêu ngôn ngữ',
    fmtIn: 'Trực tiếp', fmtOnline: 'Trực tuyến', fmtHybrid: 'Kết hợp',
    areas: { nangang: 'Nam Cảng · Academia Sinica', taipei: 'Đài Bắc (gồm NTU)', north: 'Tân Bắc, Đào Viên, Tân Trúc', south: 'Miền Trung và Nam Đài Loan', online: 'Trực tuyến' },
    langName: { en: 'Tiếng Anh', zh: 'Tiếng Trung' },
    inPlan: 'Có trong thiết lập của bạn: bạn sẽ nhận email này.',
    notInPlan: 'Không có trong thiết lập hiện tại: bạn sẽ không nhận email này.',
    mailFrom: 'Từ', mailTo: 'Đến', mailDate: 'Ngày',
    fromName: 'Bản tin sự kiện học thuật Đài Loan',
    subjectWeekly: n => `${n} sự kiện dành cho bạn tại Đài Loan`,
    subjectLast: n => `Nhắc nhở cuối: ${n} hạn đăng ký và các sự kiện sắp diễn ra`,
    hello: 'Xin chào,',
    introWeekly: n => `Đây là ${n} sự kiện sắp tới phù hợp với sở thích của bạn. Tiêu đề và tóm tắt bằng tiếng Việt; tiêu đề gốc nằm ngay bên dưới.`,
    introLast: 'Các hạn đăng ký này sắp đến, hoặc sự kiện sẽ diễn ra trong vòng 3 ngày.',
    secNext7: 'Trong 7 ngày tới', secNext30: 'Trong 8 đến 30 ngày tới', secLater: 'Sau đó, hoặc chưa nêu ngày',
    secClosing: 'Đóng đăng ký trong 14 ngày', secSoon: 'Diễn ra trong 3 ngày',
    nothing: 'Không có gì ở mục này với thiết lập của bạn.',
    manage: 'Đổi thiết lập', unsub: 'Hủy đăng ký',
    mailFoot: 'Bạn nhận email này vì đã chọn các thiết lập trên bản thử Bản tin sự kiện học thuật Đài Loan. Trong dịch vụ thật, các liên kết bên dưới là liên kết một chạm, không cần mật khẩu.',
    asOf: d => `Ngày xem thử: ${d}. Dữ liệu được thu thập vào ngày này nên bản xem thử coi đó là “hôm nay”.`,
    caveatTitle: 'Đọc trước',
    caveat: 'Nguyên mẫu sinh viên giai đoạn đầu, không phải dịch vụ chính thức. Thông tin sự kiện được đọc từ các trang công khai vào ngày 15 và 17/10/2026 và chưa được kiểm chứng độc lập. Hãy kiểm tra trang nguồn trước khi đăng ký hoặc di chuyển. Tiêu đề và tóm tắt tiếng Việt và tiếng Nhật do AI viết, chưa được người bản ngữ kiểm tra; tiêu đề gốc luôn được hiển thị.',
    notes: [
      'Không có email nào được gửi. Bản xem thử cho thấy bản tin sẽ trông thế nào; địa chỉ bạn nhập không được gửi hay lưu.',
      'Nguồn: danh sách thông báo của Wenzao (dữ liệu Nguyên mẫu 3), các trang của Đại học Quốc lập Đài Loan (NTU) và các viện của Academia Sinica (Kinh tế, Ngôn ngữ học). Chưa bao phủ mọi khoa hay viện.',
      'Thẻ chủ đề và nhãn ngôn ngữ sự kiện do chúng tôi biên soạn. “Suy đoán” nghĩa là chúng tôi đoán từ ngôn ngữ của tiêu đề hoặc tóm tắt.',
      'Tên địa điểm giữ nguyên bằng tiếng Anh. Một số sự kiện chỉ dành cho thành viên trường tổ chức; trang chỉ nói rõ khi nguồn có nói.',
      'Thiết lập của bạn được lưu trong liên kết của trang này (phần sau dấu #) và chỉ trong trình duyệt của bạn.'
    ],
    footText: 'Thuộc dự án thi AI học đường “Wenzao master’s guide”. Dự án thí điểm của sinh viên; không liên kết với các trường được nêu.'
  },
  ja: {
    skip: '本文へスキップ', brand: '台湾キャンパスイベント・ダイジェスト', back: 'プロジェクトページ',
    pill: 'プロトタイプ4・プレビューのみ(メールは送信されません)',
    heroTitle: '台湾各地の知的イベントを、あなたの言語で、受信箱へ。',
    heroLead: '台湾の大学と中央研究院(Academia Sinica)の講演、ワークショップ、学会、公開イベントを、留学生の大学院生向けに選びました。関心を一度設定すれば、English・Tiếng Việt・日本語の短いダイジェストが届きます。',
    pullEyebrow: 'プル', pullTitle: '見たいときに探す',
    pullText: 'このページが全リストです。テーマ、場所、イベントの使用言語で絞り込み、1件ずつカレンダーに追加したり、絞り込んだ一覧をカレンダーファイルとして保存したりできます。',
    pushEyebrow: 'プッシュ', pushTitle: '大事なときに届く',
    pushText: '同じ絞り込み条件がそのままニュースレターになります。毎週のダイジェストと、申込締切が近いときの最終リマインダーです。下のタブで、あなたの設定で届くメールの実際の見た目を確認できます。',
    prefsTitle: 'あなたのニュースレター',
    fInterests: '関心分野', fInterestsHint: 'いくつでも選べます。空のままなら全部表示します。',
    fWhere: '場所', fDeliv: 'イベントの使用言語',
    fDelivHint: 'ニュースレター本文は上で選んだ言語で書かれます。この絞り込みはイベント自体の使用言語についてです。',
    delivAny: 'すべての言語', delivEn: '英語', delivZh: '中国語(北京語)',
    fUnknown: '言語の記載がないイベントも表示する',
    fPlan: '受け取る内容',
    planWeekly: '毎週のダイジェスト', planBoth: '毎週のダイジェスト+最終リマインダー', planLast: '最終リマインダーのみ',
    fEmail: 'メールアドレス', fEmailHint: 'デモです。ここに入力した内容は送信も保存もされません。',
    subscribe: '登録する(デモ)', copyLink: '設定リンクをコピー', copied: 'リンクをコピーしました。', copyFail: 'コピーできませんでした。アドレスバーからコピーしてください。', reset: 'リセット',
    subscribedMsg: 'デモです。メールは送信されず、アドレスも保存されません。ほかのタブで届く内容を確認できます。',
    needEmail: '登録を試すにはメールアドレスを入力してください。どこにも送信されません。',
    tabBrowse: 'イベントを探す', tabDigest: '毎週のダイジェスト', tabLast: '最終リマインダー',
    count: (n, t) => `今後のイベント${t}件中、${n}件が該当`,
    noMatch: '該当するイベントがありません。絞り込みを減らすか、言語の記載がないイベントを表示してください。',
    icsAll: 'この一覧をカレンダー(.ics)で保存', addCal: 'カレンダーに追加', source: '情報元ページ', register: '申込み・詳細',
    deadline: '締切', dateTbc: '日付の記載なし', timeNotStated: '時間の記載なし',
    langStated: l => l, langInferred: l => `${l}(推測)`, langUnknown: '言語の記載なし',
    fmtIn: '対面', fmtOnline: 'オンライン', fmtHybrid: 'ハイブリッド',
    areas: { nangang: '南港・中央研究院', taipei: '台北市内(台大を含む)', north: '新北・桃園・新竹', south: '台湾中部・南部', online: 'オンライン' },
    langName: { en: '英語', zh: '中国語' },
    inPlan: 'あなたの設定に含まれます:このメールが届きます。',
    notInPlan: '現在の設定には含まれません:このメールは届きません。',
    mailFrom: '差出人', mailTo: '宛先', mailDate: '日付',
    fromName: '台湾キャンパスイベント・ダイジェスト',
    subjectWeekly: n => `台湾であなた向けのイベント${n}件`,
    subjectLast: n => `最終案内:申込締切${n}件と間もなく始まるイベント`,
    hello: 'こんにちは。',
    introWeekly: n => `あなたの関心に合う今後のイベントを${n}件お届けします。タイトルと概要は日本語で、元のタイトルを各項目の下に載せています。`,
    introLast: '申込締切が近いもの、または3日以内に始まるイベントです。',
    secNext7: '今後7日以内', secNext30: '8〜30日後', secLater: 'それ以降・日付の記載なし',
    secClosing: '14日以内に申込締切', secSoon: '3日以内に開始',
    nothing: 'この設定では該当するものはありません。',
    manage: '設定を変更', unsub: '配信停止',
    mailFoot: 'このメールは、台湾キャンパスイベント・ダイジェストのプロトタイプでこの設定を選んだため届いています。実際のサービスでは、下のリンクはパスワード不要のワンクリックリンクになります。',
    asOf: d => `プレビュー日:${d}。データはこの日に収集したため、プレビューではこの日を「今日」として扱います。`,
    caveatTitle: '最初にお読みください',
    caveat: '学生による初期のプロトタイプで、公式サービスではありません。イベント情報は2026年10月15日・17日に公開ページから読み取ったもので、第三者による検証は行っていません。申込みや移動の前に必ず情報元ページを確認してください。ベトナム語と日本語のタイトル・概要はAIが作成したもので、ネイティブによる確認はしていません。元のタイトルは常に表示します。',
    notes: [
      'メールは送信されません。プレビューはダイジェストの見た目を示すもので、入力したアドレスは送信も保存もされません。',
      '情報源:文藻外語大学のお知らせ一覧(プロトタイプ3のデータ)、国立台湾大学(NTU)のページ、中央研究院の研究所ページ(経済学・言語学)。すべての学科・研究所を網羅してはいません。',
      'テーマのタグとイベント言語のラベルは当方の整理です。「推測」はタイトルや概要の言語から判断したものです。',
      '会場名は英語のままです。主催校の構成員限定のイベントもありますが、情報源に記載があるものだけページに明記しています。',
      'あなたの設定は、このページのリンク(#以降)とお使いのブラウザにのみ保存されます。'
    ],
    footText: 'キャンパスAIコンテスト・プロジェクト「Wenzao master’s guide」の一部。学生のパイロットで、掲載大学とは無関係です。'
  }
};

// ---------- state ----------
const AREAS = ['nangang', 'taipei', 'north', 'south', 'online'];
const DEFAULTS = () => ({ lang: 'en', topics: [], areas: [], deliv: 'any', unk: true, plan: 'both', tab: 'browse' });
let state = DEFAULTS();
let DATA = null;
const $ = id => document.getElementById(id);
const L = () => T[state.lang];

function loadState() {
  try {
    const h = new URLSearchParams(location.hash.slice(1));
    if (h.has('l') && T[h.get('l')]) state.lang = h.get('l');
    else {
      const n = (navigator.language || 'en').slice(0, 2);
      if (T[n]) state.lang = n;
    }
    if (h.get('t')) state.topics = h.get('t').split(',').filter(Boolean);
    if (h.get('a')) state.areas = h.get('a').split(',').filter(x => AREAS.includes(x));
    if (['any', 'en', 'zh'].includes(h.get('d'))) state.deliv = h.get('d');
    if (h.get('u') === '0') state.unk = false;
    if (['weekly', 'both', 'last'].includes(h.get('p'))) state.plan = h.get('p');
    if (['browse', 'digest', 'last'].includes(h.get('v'))) state.tab = h.get('v');
  } catch (e) { /* defaults */ }
}
function saveState() {
  const h = new URLSearchParams();
  h.set('l', state.lang);
  if (state.topics.length) h.set('t', state.topics.join(','));
  if (state.areas.length) h.set('a', state.areas.join(','));
  if (state.deliv !== 'any') h.set('d', state.deliv);
  if (!state.unk) h.set('u', '0');
  if (state.plan !== 'both') h.set('p', state.plan);
  if (state.tab !== 'browse') h.set('v', state.tab);
  try { history.replaceState(null, '', '#' + h.toString()); } catch (e) { /* ignore */ }
}

// ---------- helpers ----------
const esc = s => String(s == null ? '' : s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const asOf = () => DATA.as_of;
const dayDiff = (a, b) => Math.round((Date.parse(b + 'T00:00:00Z') - Date.parse(a + 'T00:00:00Z')) / 864e5);
function fmtDate(iso, opts) {
  if (!iso) return '';
  return new Intl.DateTimeFormat(state.lang, Object.assign({ timeZone: 'UTC' }, opts || { year: 'numeric', month: 'short', day: 'numeric', weekday: 'short' })).format(new Date(iso + 'T00:00:00Z'));
}
const title = e => e.title[state.lang] || e.title.en;
const blurb = e => e.blurb[state.lang] || e.blurb.en;
const note = e => e.note ? (e.note[state.lang] || e.note.en) : '';
const cityName = c => c ? ((DATA.cities[c] || {})[state.lang] || c) : '';
const nextSession = e => e.sessions.find(s => s.date && (s.end_date || s.date) >= asOf()) || e.sessions.find(s => s.date) || null;
const eventDate = e => { const s = nextSession(e); return s ? s.date : null; };

function dateLine(e) {
  const parts = e.sessions.filter(s => s.date).map(s => {
    let d = fmtDate(s.date);
    if (s.end_date) d += ' – ' + fmtDate(s.end_date);
    if (s.time) d += ' · ' + s.time.replace('-', '–');
    return d;
  });
  return parts.length ? parts : [L().dateTbc];
}
function placeLine(e) {
  const seen = new Set();
  const out = [];
  e.sessions.forEach(s => {
    const p = [s.venue_en, cityName(s.city_en)].filter(Boolean).join(', ');
    if (p && !seen.has(p)) { seen.add(p); out.push(p); }
  });
  return out;
}
function langLabel(e) {
  const l = e.language;
  if (!l.value) return L().langUnknown;
  const name = L().langName[l.value] || l.value;
  return l.basis === 'inferred' ? L().langInferred(name) : L().langStated(name);
}
function fmtLabel(e) { return e.format === 'online' ? L().fmtOnline : e.format === 'hybrid' ? L().fmtHybrid : e.format === 'in-person' ? L().fmtIn : ''; }

function matches(e) {
  if (state.topics.length && !e.topics.some(t => state.topics.includes(t))) return false;
  if (state.areas.length && !state.areas.includes(e.area)) return false;
  if (state.deliv !== 'any') {
    const v = e.language.value;
    if (v ? v !== state.deliv : !state.unk) return false;
  }
  return true;
}
const matched = () => DATA.events.filter(matches);

// ---------- calendar (.ics) ----------
const icsEsc = s => String(s || '').replace(/\\/g, '\\\\').replace(/;/g, '\\;').replace(/,/g, '\\,').replace(/\r?\n/g, '\\n');
const ymd = iso => iso.replace(/-/g, '');
function addDay(iso, n) { const d = new Date(iso + 'T00:00:00Z'); d.setUTCDate(d.getUTCDate() + n); return d.toISOString().slice(0, 10); }
function veventsFor(e) {
  const out = [];
  e.sessions.filter(s => s.date).forEach((s, i) => {
    const lines = ['BEGIN:VEVENT', `UID:${e.id}-${i}@campus-events-digest.prototype`, `DTSTAMP:${ymd(asOf())}T000000Z`,
      `SUMMARY:${icsEsc(e.title.en)}`];
    const m = s.time && s.time.match(/^(\d\d):(\d\d)(?:-(\d\d):(\d\d))?$/);
    if (m) {
      lines.push(`DTSTART;TZID=Asia/Taipei:${ymd(s.date)}T${m[1]}${m[2]}00`);
      if (m[3]) lines.push(`DTEND;TZID=Asia/Taipei:${ymd(s.end_date || s.date)}T${m[3]}${m[4]}00`);
    } else {
      lines.push(`DTSTART;VALUE=DATE:${ymd(s.date)}`, `DTEND;VALUE=DATE:${ymd(addDay(s.end_date || s.date, 1))}`);
    }
    const loc = [s.venue_en, s.city_en].filter(Boolean).join(', ');
    if (loc) lines.push(`LOCATION:${icsEsc(loc)}`);
    lines.push(`DESCRIPTION:${icsEsc(e.blurb.en + ' Check the source page before you go: ' + e.url)}`, `URL:${e.url}`, 'END:VEVENT');
    out.push(lines.join('\r\n'));
  });
  return out;
}
function buildIcs(events) {
  const v = events.flatMap(veventsFor);
  if (!v.length) return null;
  return ['BEGIN:VCALENDAR', 'VERSION:2.0', 'PRODID:-//Taiwan Campus Events Digest prototype//EN', 'CALSCALE:GREGORIAN',
    'BEGIN:VTIMEZONE', 'TZID:Asia/Taipei', 'BEGIN:STANDARD', 'DTSTART:19700101T000000', 'TZOFFSETFROM:+0800', 'TZOFFSETTO:+0800', 'TZNAME:CST', 'END:STANDARD', 'END:VTIMEZONE',
    ...v, 'END:VCALENDAR'].join('\r\n');
}
function download(name, text) {
  const url = URL.createObjectURL(new Blob([text], { type: 'text/calendar;charset=utf-8' }));
  const a = document.createElement('a');
  a.href = url; a.download = name; document.body.appendChild(a); a.click(); a.remove();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}

// ---------- rendering ----------
function renderStatic() {
  const t = L();
  document.documentElement.lang = state.lang;
  document.querySelectorAll('[data-i18n]').forEach(el => { const v = t[el.dataset.i18n]; if (typeof v === 'string') el.textContent = v; });
  document.querySelectorAll('#langSwitch button').forEach(b => b.setAttribute('aria-pressed', String(b.dataset.lang === state.lang)));
  document.title = t.brand + ' (prototype)';
  $('tab-browse').textContent = t.tabBrowse; $('tab-digest').textContent = t.tabDigest; $('tab-last').textContent = t.tabLast;
  $('icsAll').textContent = t.icsAll;
  $('caveat').innerHTML = `<strong>${esc(t.caveatTitle)}.</strong> ${esc(t.caveat)}`;
  $('notesList').innerHTML = t.notes.map(n => `<li>${esc(n)}</li>`).join('') + `<li>${esc(t.asOf(fmtDate(asOf(), { year: 'numeric', month: 'long', day: 'numeric' })))}</li>`;
  $('footText').textContent = t.footText;

  $('topicChips').innerHTML = Object.keys(DATA.topics).map(k =>
    `<button type="button" class="chip" data-topic="${k}" aria-pressed="${state.topics.includes(k)}">${esc(DATA.topics[k][state.lang])}</button>`).join('');
  $('areaChecks').innerHTML = AREAS.map(a =>
    `<label class="check"><input type="checkbox" data-area="${a}" ${state.areas.includes(a) ? 'checked' : ''}> <span>${esc(t.areas[a])}</span></label>`).join('');
  $('delivRadios').innerHTML = [['any', t.delivAny], ['en', t.delivEn], ['zh', t.delivZh]].map(([v, lab]) =>
    `<label class="opt"><input type="radio" name="deliv" value="${v}" ${state.deliv === v ? 'checked' : ''}> <span>${esc(lab)}</span></label>`).join('');
  $('inclUnknown').checked = state.unk;
  $('planRadios').innerHTML = [['weekly', t.planWeekly], ['both', t.planBoth], ['last', t.planLast]].map(([v, lab]) =>
    `<label class="opt"><input type="radio" name="plan" value="${v}" ${state.plan === v ? 'checked' : ''}> <span>${esc(lab)}</span></label>`).join('');
}

function cardHtml(e) {
  const t = L();
  const dl = e.deadline;
  const dlDays = dl ? dayDiff(asOf(), dl) : null;
  const tags = [`<span class="tag kind">${esc(DATA.kinds[e.kind][state.lang])}</span>`];
  const f = fmtLabel(e); if (f) tags.push(`<span class="tag">${esc(f)}</span>`);
  tags.push(`<span class="tag lang">${esc(langLabel(e))}</span>`);
  e.topics.forEach(k => tags.push(`<span class="tag">${esc(DATA.topics[k][state.lang])}</span>`));
  if (dl) tags.push(`<span class="tag ${dlDays <= 7 ? 'warn' : ''}">${esc(t.deadline)}: ${esc(fmtDate(dl, { month: 'short', day: 'numeric', year: 'numeric' }))}</span>`);
  const orig = e.title.orig && e.title.orig !== title(e) ? `<p class="orig" lang="${/[\u4e00-\u9fff]/.test(e.title.orig) ? 'zh-Hant' : 'en'}">${esc(e.title.orig)}</p>` : '';
  const places = placeLine(e);
  const hasCal = e.sessions.some(s => s.date);
  return `<li class="ev"><div class="tags">${tags.join('')}</div>
    <h3>${esc(title(e))}</h3>${orig}
    <div class="meta"><span><b>${dateLine(e).map(esc).join('; ')}</b></span>${places.length ? `<span>${places.map(esc).join('; ')}</span>` : ''}<span>${esc(e.organizer_en)}</span></div>
    <p class="blurb">${esc(blurb(e))}</p>
    ${note(e) ? `<p class="note">${esc(note(e))}</p>` : ''}
    <div class="acts"><a class="btn small" href="${esc(e.url)}" target="_blank" rel="noopener">${esc(t.source)} ↗</a>
    ${e.register_url ? `<a class="btn small" href="${esc(e.register_url)}" target="_blank" rel="noopener">${esc(t.register)} ↗</a>` : ''}
    ${hasCal ? `<button type="button" class="btn small" data-ics="${esc(e.id)}">${esc(t.addCal)}</button>` : ''}</div></li>`;
}

function renderBrowse() {
  const m = matched();
  $('count').textContent = L().count(m.length, DATA.events.length);
  $('icsAll').disabled = !m.some(e => e.sessions.some(s => s.date));
  $('list').innerHTML = m.length ? m.map(cardHtml).join('') : `<li class="empty">${esc(L().noMatch)}</li>`;
}

function mailItem(e, withWarn) {
  const t = L();
  const orig = e.title.orig && e.title.orig !== title(e) ? `<p class="o">${esc(e.title.orig)}</p>` : '';
  const dl = e.deadline ? `<span class="w">${esc(t.deadline)} ${esc(fmtDate(e.deadline, { month: 'short', day: 'numeric' }))}</span>` : '';
  const places = placeLine(e);
  return `<div class="item"><a class="t" href="${esc(e.url)}" onclick="return false">${esc(title(e))}</a>${withWarn ? dl : ''}
    ${orig}<p class="m">${dateLine(e).map(esc).join('; ')}${places.length ? ' · ' + esc(places[0]) : ''} · ${esc(langLabel(e))}</p>
    <p class="b">${esc(blurb(e))}</p></div>`;
}
function mailFrame(subject, intro, sections) {
  const t = L();
  const secs = sections.map(([h, items, warn]) => `<h4>${esc(h)}</h4>${items.length ? items.map(e => mailItem(e, warn)).join('') : `<p class="none">${esc(t.nothing)}</p>`}`).join('');
  return `<div class="head"><p class="subj">${esc(subject)}</p>
    <p>${esc(t.mailFrom)}: ${esc(t.fromName)} &lt;digest@example.invalid&gt;</p>
    <p>${esc(t.mailTo)}: ${esc($('email').value.trim() || 'you@example.com')}</p>
    <p>${esc(t.mailDate)}: ${esc(fmtDate(asOf(), { year: 'numeric', month: 'long', day: 'numeric' }))}</p></div>
    <div class="body"><h3>${esc(t.fromName)}</h3><p>${esc(t.hello)}</p><p>${esc(intro)}</p>${secs}
    <div class="foot"><p>${esc(t.mailFoot)}</p><p><a href="#" onclick="return false">${esc(t.manage)}</a> · <a href="#" onclick="return false">${esc(t.unsub)}</a></p></div></div>`;
}

function renderDigest() {
  const t = L(), m = matched();
  const upcoming = e => { const d = eventDate(e); return d == null ? 9999 : dayDiff(asOf(), d); };
  const b1 = m.filter(e => upcoming(e) <= 7), b2 = m.filter(e => upcoming(e) > 7 && upcoming(e) <= 30), b3 = m.filter(e => upcoming(e) > 30);
  const inPlan = state.plan !== 'last';
  $('planDigest').innerHTML = `<b>${esc(inPlan ? t.inPlan : t.notInPlan)}</b>`;
  $('digestMail').innerHTML = mailFrame(t.subjectWeekly(m.length), t.introWeekly(m.length),
    [[t.secNext7, b1, true], [t.secNext30, b2, true], [t.secLater, b3, true]]);
}

function renderLast() {
  const t = L(), m = matched();
  const closing = m.filter(e => e.deadline && dayDiff(asOf(), e.deadline) >= 0 && dayDiff(asOf(), e.deadline) <= 14)
    .sort((a, b) => a.deadline.localeCompare(b.deadline));
  const soon = m.filter(e => { const d = eventDate(e); return d != null && dayDiff(asOf(), d) >= 0 && dayDiff(asOf(), d) <= 3; });
  const inPlan = state.plan !== 'weekly';
  $('planLast').innerHTML = `<b>${esc(inPlan ? t.inPlan : t.notInPlan)}</b>`;
  $('lastMail').innerHTML = mailFrame(t.subjectLast(closing.length), t.introLast,
    [[t.secClosing, closing, true], [t.secSoon, soon, true]]);
}

function renderTabs() {
  ['browse', 'digest', 'last'].forEach(k => {
    const on = state.tab === k;
    const b = $('tab-' + k);
    b.setAttribute('aria-selected', String(on)); b.tabIndex = on ? 0 : -1;
    $('panel-' + k).hidden = !on;
  });
}

function renderAll() {
  renderStatic(); renderTabs(); renderBrowse(); renderDigest(); renderLast(); saveState();
}
function renderResults() { renderBrowse(); renderDigest(); renderLast(); saveState(); }

// ---------- events ----------
function bind() {
  $('langSwitch').addEventListener('click', ev => {
    const b = ev.target.closest('button[data-lang]'); if (!b) return;
    state.lang = b.dataset.lang; renderAll();
  });
  $('topicChips').addEventListener('click', ev => {
    const b = ev.target.closest('[data-topic]'); if (!b) return;
    const k = b.dataset.topic; const i = state.topics.indexOf(k);
    if (i >= 0) state.topics.splice(i, 1); else state.topics.push(k);
    b.setAttribute('aria-pressed', String(i < 0)); renderResults();
  });
  $('areaChecks').addEventListener('change', ev => {
    const c = ev.target.closest('[data-area]'); if (!c) return;
    state.areas = Array.from(document.querySelectorAll('[data-area]:checked')).map(x => x.dataset.area); renderResults();
  });
  $('delivRadios').addEventListener('change', ev => { if (ev.target.name === 'deliv') { state.deliv = ev.target.value; renderResults(); } });
  $('planRadios').addEventListener('change', ev => { if (ev.target.name === 'plan') { state.plan = ev.target.value; renderResults(); } });
  $('inclUnknown').addEventListener('change', ev => { state.unk = ev.target.checked; renderResults(); });
  $('email').addEventListener('input', () => { renderDigest(); renderLast(); });
  $('prefs').addEventListener('submit', ev => {
    ev.preventDefault();
    const msg = $('formMsg'), email = $('email');
    if (!email.value.trim() || !email.checkValidity()) { msg.className = 'msg'; msg.textContent = L().needEmail; email.focus(); return; }
    msg.className = 'msg ok'; msg.textContent = L().subscribedMsg;
    state.tab = state.plan === 'last' ? 'last' : 'digest'; renderTabs(); saveState();
  });
  $('copyLink').addEventListener('click', async () => {
    saveState(); const msg = $('formMsg');
    try { await navigator.clipboard.writeText(location.href); msg.className = 'msg ok'; msg.textContent = L().copied; }
    catch (e) { msg.className = 'msg'; msg.textContent = L().copyFail; }
  });
  $('reset').addEventListener('click', () => {
    const lang = state.lang; state = DEFAULTS(); state.lang = lang; $('email').value = ''; $('formMsg').textContent = ''; renderAll();
  });
  document.querySelector('.tabs').addEventListener('click', ev => {
    const b = ev.target.closest('[data-tab]'); if (!b) return;
    state.tab = b.dataset.tab; renderTabs(); saveState();
  });
  document.querySelector('.tabs').addEventListener('keydown', ev => {
    if (ev.key !== 'ArrowRight' && ev.key !== 'ArrowLeft') return;
    const order = ['browse', 'digest', 'last'];
    const i = (order.indexOf(state.tab) + (ev.key === 'ArrowRight' ? 1 : 2)) % 3;
    state.tab = order[i]; renderTabs(); $('tab-' + state.tab).focus(); saveState();
  });
  $('list').addEventListener('click', ev => {
    const b = ev.target.closest('[data-ics]'); if (!b) return;
    const e = DATA.events.find(x => x.id === b.dataset.ics); const ics = e && buildIcs([e]);
    if (ics) download(e.id + '.ics', ics);
  });
  $('icsAll').addEventListener('click', () => { const ics = buildIcs(matched()); if (ics) download('taiwan-campus-events.ics', ics); });
}

loadState();
fetch('data/events.json').then(r => { if (!r.ok) throw new Error(r.status); return r.json(); }).then(d => {
  DATA = d; bind(); renderAll();
}).catch(err => {
  $('list').innerHTML = `<li class="empty">Could not load data/events.json (${esc(err.message)}). Serve this folder over http, for example with python3 -m http.server.</li>`;
});
})();
