const renderers = new marked.Renderer();
let labelList = [];
const renderer = {
  code(code, infostring, escaped) {
    const lang = (infostring || "").match(/\S*/)[0];
    if (this.options.highlight) {
      const out = this.options.highlight(code, lang);
      if (out != null && out !== code) {
        escaped = true;
        code = out;
      }
    }

    if (!lang) {
      return (
        '<pre class="line-numbers"><code>' +
        (escaped ? code : escape(code, true)) +
        "</code></pre>\n"
      );
    }
    let labelItem =
      '<a class="ui teal right ribbon label sing-' +
      lang +
      '">' +
      lang.toUpperCase() +
      "</a>";

    labelList.push(labelItem);
    let mbData =
      `<pre class="line-numbers"><code class="` +
      this.options.langPrefix +
      escape(lang, true) +
      '">' +
      (escaped ? code : escape(code, true)) +
      "</code></pre>\n";
    return mbData;
  },
};

marked.setOptions({
  renderer: renderers,
  highlight: function (code) {
    return hljs.highlightAuto(code).value;
  },
  pedantic: false,
  gfm: true,
  breaks: false,
  sanitize: false,
  smartLists: true,
  smartypants: false,
  xhtml: false,
});
marked.use({ renderer });
var a = $("#mb-data").text();
document.getElementById("mbed-data").innerHTML = marked(a);

(function codeHight() {
  if (!window.Prism || !document.querySelectorAll) {
    return;
  }

  function $$(expr, con) {
    return Array.prototype.slice.call((con || document).querySelectorAll(expr));
  }

  function numberLines(pre) {
    var offset = +pre.getAttribute("data-line-offset") || 0;
    var lineHeight = parseFloat(getComputedStyle(pre).lineHeight);
    var code = pre.querySelector("code");
    var numLines = code.innerHTML.split("\n").length;
    pre.setAttribute("data-number", "");

    for (var i = 1; i <= numLines; i++) {
      var line = document.createElement("div");
      line.className = "line-number";
      line.setAttribute("data-start", i);
      line.style.top = (i - offset - 1) * lineHeight + "px";

      (code || pre).appendChild(line);
    }
  }

  Prism.hooks.add("after-highlight", function (env) {
    var pre = env.element.parentNode;

    if (!pre || !/pre/i.test(pre.nodeName)) {
      return;
    }

    $$(".line-number", pre).forEach(function (line) {
      line.parentNode.removeChild(line);
    });

    numberLines(pre);
  });
})();

console.log(labelList);

function addLabel() {
  var itemList = $(".code-toolbar");
  console.log(itemList);
}
addLabel();
