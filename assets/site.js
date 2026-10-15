(function () {
  var btn = document.getElementById('copy-btn');
  if (!btn) return;
  var status = document.getElementById('copy-status');
  var src = document.getElementById('prompt-text');
  function say(msg) { status.textContent = msg; }
  btn.addEventListener('click', function () {
    var text = src.textContent.trim();
    function fallback() {
      var r = document.createRange();
      r.selectNodeContents(src);
      var s = window.getSelection();
      s.removeAllRanges(); s.addRange(r);
      var ok = false;
      try { ok = document.execCommand('copy'); } catch (e) {}
      say(ok ? 'Copied.' : 'Text selected. Press Ctrl+C (Cmd+C on Mac) to copy.');
    }
    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(text).then(function () { say('Copied.'); }, fallback);
    } else { fallback(); }
  });
})();
