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
      '<a class="ui right ribbon label sing-' +
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

function parseDom(arg) {
  var objE = document.createElement("div");

  objE.innerHTML = arg;

  return objE.childNodes;
}
function addLabel() {
  var itemList = $(".code-toolbar");

  for (let i = 0; i < itemList.length; i++) {
    itemList[i].prepend(parseDom(labelList[i])[0]);
  }
}
document.onreadystatechange = function () {
  if (document.readyState == "complete") {
    addLabel();
  }
};
