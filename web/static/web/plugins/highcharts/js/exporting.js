/**
 * Highcharts JS v11.3.0 (2024-01-10)
 *
 * Exporting module
 *
 * (c) 2010-2024 Torstein Honsi
 *
 * License: www.highcharts.com/license
 */!function (e) {
    "object" == typeof module && module.exports ? (e.default = e, module.exports = e) : "function" == typeof define && define.amd ? define("highcharts/modules/exporting", ["highcharts"], function (t) {
        return e(t), e.Highcharts = t, e
    }) : e("undefined" != typeof Highcharts ? Highcharts : void 0)
}(function (e) {
    "use strict";
    var t = e ? e._modules : {};

    function n(e, t, n, i) {
        e.hasOwnProperty(t) || (e[t] = i.apply(null, n), "function" == typeof CustomEvent && window.dispatchEvent(new CustomEvent("HighchartsModuleLoaded", {
            detail: {
                path: t,
                module: e[t]
            }
        })))
    }

    n(t, "Core/Chart/ChartNavigationComposition.js", [], function () {
        var e;
        return function (e) {
            e.compose = function (e) {
                return e.navigation || (e.navigation = new t(e)), e
            };

            class t {
                constructor(e) {
                    this.updates = [], this.chart = e
                }

                addUpdate(e) {
                    this.chart.navigation.updates.push(e)
                }

                update(e, t) {
                    this.updates.forEach(n => {
                        n.call(this.chart, e, t)
                    })
                }
            }

            e.Additions = t
        }(e || (e = {})), e
    }), n(t, "Extensions/Exporting/ExportingDefaults.js", [t["Core/Globals.js"]], function (e) {
        let {isTouchDevice: t} = e;
        return {
            exporting: {
                allowTableSorting: !0,
                type: "image/png",
                url: "https://export.highcharts.com/",
                pdfFont: {normal: void 0, bold: void 0, bolditalic: void 0, italic: void 0},
                printMaxWidth: 780,
                scale: 2,
                buttons: {
                    contextButton: {
                        className: "highcharts-contextbutton",
                        menuClassName: "highcharts-contextmenu",
                        symbol: "menu",
                        titleKey: "contextButtonTitle",
                        menuItems: ["viewFullscreen", "printChart", "separator", "downloadPNG", "downloadJPEG", "downloadPDF", "downloadSVG"]
                    }
                },
                menuItemDefinitions: {
                    viewFullscreen: {
                        textKey: "viewFullscreen", onclick: function () {
                            this.fullscreen && this.fullscreen.toggle()
                        }
                    }, printChart: {
                        textKey: "printChart", onclick: function () {
                            this.print()
                        }
                    }, separator: {separator: !0}, downloadPNG: {
                        textKey: "downloadPNG", onclick: function () {
                            this.exportChart()
                        }
                    }, downloadJPEG: {
                        textKey: "downloadJPEG", onclick: function () {
                            this.exportChart({type: "image/jpeg"})
                        }
                    }, downloadPDF: {
                        textKey: "downloadPDF", onclick: function () {
                            this.exportChart({type: "application/pdf"})
                        }
                    }, downloadSVG: {
                        textKey: "downloadSVG", onclick: function () {
                            this.exportChart({type: "image/svg+xml"})
                        }
                    }
                }
            },
            lang: {
                viewFullscreen: "View in full screen",
                exitFullscreen: "Exit from full screen",
                printChart: "Print chart",
                downloadPNG: "Download PNG image",
                downloadJPEG: "Download JPEG image",
                downloadPDF: "Download PDF document",
                downloadSVG: "Download SVG vector image",
                contextButtonTitle: "Chart context menu"
            },
            navigation: {
                buttonOptions: {
                    symbolSize: 14,
                    symbolX: 14.5,
                    symbolY: 13.5,
                    align: "right",
                    buttonSpacing: 3,
                    height: 28,
                    verticalAlign: "top",
                    width: 28,
                    symbolFill: "#666666",
                    symbolStroke: "#666666",
                    symbolStrokeWidth: 3,
                    theme: {padding: 5}
                },
                menuStyle: {border: "none", borderRadius: "3px", background: "#ffffff", padding: "0.5em"},
                menuItemStyle: {
                    background: "none",
                    borderRadius: "3px",
                    color: "#333333",
                    padding: "0.5em",
                    fontSize: t ? "0.9em" : "0.8em",
                    transition: "background 250ms, color 250ms"
                },
                menuItemHoverStyle: {background: "#f2f2f2"}
            }
        }
    }), n(t, "Extensions/Exporting/ExportingSymbols.js", [], function () {
        var e;
        return function (e) {
            let t = [];

            function n(e, t, n, i) {
                return [["M", e, t + 2.5], ["L", e + n, t + 2.5], ["M", e, t + i / 2 + .5], ["L", e + n, t + i / 2 + .5], ["M", e, t + i - 1.5], ["L", e + n, t + i - 1.5]]
            }

            function i(e, t, n, i) {
                let o = i / 3 - 2;
                return [].concat(this.circle(n - o, t, o, o), this.circle(n - o, t + o + 4, o, o), this.circle(n - o, t + 2 * (o + 4), o, o))
            }

            e.compose = function (e) {
                if (-1 === t.indexOf(e)) {
                    t.push(e);
                    let o = e.prototype.symbols;
                    o.menu = n, o.menuball = i.bind(o)
                }
            }
        }(e || (e = {})), e
    }), n(t, "Extensions/Exporting/Fullscreen.js", [t["Core/Renderer/HTML/AST.js"], t["Core/Globals.js"], t["Core/Utilities.js"]], function (e, t, n) {
        let {composed: i} = t, {addEvent: o, fireEvent: r, pushUnique: s} = n;

        function l() {
            this.fullscreen = new a(this)
        }

        class a {
            static compose(e) {
                s(i, this.compose) && o(e, "beforeRender", l)
            }

            constructor(e) {
                this.chart = e, this.isOpen = !1;
                let t = e.renderTo;
                !this.browserProps && ("function" == typeof t.requestFullscreen ? this.browserProps = {
                    fullscreenChange: "fullscreenchange",
                    requestFullscreen: "requestFullscreen",
                    exitFullscreen: "exitFullscreen"
                } : t.mozRequestFullScreen ? this.browserProps = {
                    fullscreenChange: "mozfullscreenchange",
                    requestFullscreen: "mozRequestFullScreen",
                    exitFullscreen: "mozCancelFullScreen"
                } : t.webkitRequestFullScreen ? this.browserProps = {
                    fullscreenChange: "webkitfullscreenchange",
                    requestFullscreen: "webkitRequestFullScreen",
                    exitFullscreen: "webkitExitFullscreen"
                } : t.msRequestFullscreen && (this.browserProps = {
                    fullscreenChange: "MSFullscreenChange",
                    requestFullscreen: "msRequestFullscreen",
                    exitFullscreen: "msExitFullscreen"
                }))
            }

            close() {
                let e = this, t = e.chart, n = t.options.chart;
                r(t, "fullscreenClose", null, function () {
                    e.isOpen && e.browserProps && t.container.ownerDocument instanceof Document && t.container.ownerDocument[e.browserProps.exitFullscreen](), e.unbindFullscreenEvent && (e.unbindFullscreenEvent = e.unbindFullscreenEvent()), t.setSize(e.origWidth, e.origHeight, !1), e.origWidth = void 0, e.origHeight = void 0, n.width = e.origWidthOption, n.height = e.origHeightOption, e.origWidthOption = void 0, e.origHeightOption = void 0, e.isOpen = !1, e.setButtonText()
                })
            }

            open() {
                let e = this, t = e.chart, n = t.options.chart;
                r(t, "fullscreenOpen", null, function () {
                    if (n && (e.origWidthOption = n.width, e.origHeightOption = n.height), e.origWidth = t.chartWidth, e.origHeight = t.chartHeight, e.browserProps) {
                        let n = o(t.container.ownerDocument, e.browserProps.fullscreenChange, function () {
                            e.isOpen ? (e.isOpen = !1, e.close()) : (t.setSize(null, null, !1), e.isOpen = !0, e.setButtonText())
                        }), i = o(t, "destroy", n);
                        e.unbindFullscreenEvent = () => {
                            n(), i()
                        };
                        let r = t.renderTo[e.browserProps.requestFullscreen]();
                        r && r.catch(function () {
                            alert("Full screen is not supported inside a frame.")
                        })
                    }
                })
            }

            setButtonText() {
                let t = this.chart, n = t.exportDivElements, i = t.options.exporting,
                    o = i && i.buttons && i.buttons.contextButton.menuItems, r = t.options.lang;
                if (i && i.menuItemDefinitions && r && r.exitFullscreen && r.viewFullscreen && o && n) {
                    let t = n[o.indexOf("viewFullscreen")];
                    t && e.setElementHTML(t, this.isOpen ? r.exitFullscreen : i.menuItemDefinitions.viewFullscreen.text || r.viewFullscreen)
                }
            }

            toggle() {
                this.isOpen ? this.close() : this.open()
            }
        }

        return a
    }), n(t, "Core/HttpUtilities.js", [t["Core/Globals.js"], t["Core/Utilities.js"]], function (e, t) {
        let {doc: n, win: i} = e, {createElement: o, discardElement: r, merge: s, objectEach: l} = t, a = {
            ajax: function (e) {
                let t = {
                    json: "application/json",
                    xml: "application/xml",
                    text: "text/plain",
                    octet: "application/octet-stream"
                }, n = new XMLHttpRequest;

                function i(t, n) {
                    e.error && e.error(t, n)
                }

                if (!e.url) return !1;
                n.open((e.type || "get").toUpperCase(), e.url, !0), e.headers && e.headers["Content-Type"] || n.setRequestHeader("Content-Type", t[e.dataType || "json"] || t.text), l(e.headers, function (e, t) {
                    n.setRequestHeader(t, e)
                }), e.responseType && (n.responseType = e.responseType), n.onreadystatechange = function () {
                    let t;
                    if (4 === n.readyState) {
                        if (200 === n.status) {
                            if ("blob" !== e.responseType && (t = n.responseText, "json" === e.dataType)) try {
                                t = JSON.parse(t)
                            } catch (e) {
                                if (e instanceof Error) return i(n, e)
                            }
                            return e.success && e.success(t, n)
                        }
                        i(n, n.responseText)
                    }
                }, e.data && "string" != typeof e.data && (e.data = JSON.stringify(e.data)), n.send(e.data)
            }, getJSON: function (e, t) {
                a.ajax({url: e, success: t, dataType: "json", headers: {"Content-Type": "text/plain"}})
            }, post: function (e, t, n) {
                let o = new i.FormData;
                l(t, function (e, t) {
                    o.append(t, e)
                }), o.append("b64", "true");
                let {filename: s, type: a} = t;
                return i.fetch(e, {method: "POST", body: o, ...n}).then(e => {
                    e.ok && e.text().then(e => {
                        let t = document.createElement("a");
                        t.href = `data:${a};base64,${e}`, t.download = s, t.click(), r(t)
                    })
                })
            }
        };
        return a
    }), n(t, "Extensions/Exporting/Exporting.js", [t["Core/Renderer/HTML/AST.js"], t["Core/Chart/Chart.js"], t["Core/Chart/ChartNavigationComposition.js"], t["Core/Defaults.js"], t["Extensions/Exporting/ExportingDefaults.js"], t["Extensions/Exporting/ExportingSymbols.js"], t["Extensions/Exporting/Fullscreen.js"], t["Core/Globals.js"], t["Core/HttpUtilities.js"], t["Core/Utilities.js"]], function (e, t, n, i, o, r, s, l, a, c) {
        var p;
        let {defaultOptions: u, setOptions: h} = i, {composed: d, doc: g, SVG_NS: f, win: m} = l, {
            addEvent: x,
            css: y,
            createElement: b,
            discardElement: v,
            extend: w,
            find: E,
            fireEvent: C,
            isObject: S,
            merge: T,
            objectEach: F,
            pick: O,
            pushUnique: k,
            removeEvent: M,
            uniqueKey: P
        } = c;
        return function (t) {
            let i;
            let p = [/-/, /^(clipPath|cssText|d|height|width)$/, /^font$/, /[lL]ogical(Width|Height)$/, /^parentRule$/, /^(cssRules|ownerRules)$/, /perspective/, /TapHighlightColor/, /^transition/, /^length$/, /^[0-9]+$/],
                h = ["fill", "stroke", "strokeLinecap", "strokeLinejoin", "strokeWidth", "textAnchor", "x", "y"];
            t.inlineAllowlist = [];
            let N = ["clipPath", "defs", "desc"];

            function j(e) {
                let t, n;
                let i = this, o = i.renderer, r = T(i.options.navigation.buttonOptions, e), s = r.onclick,
                    l = r.menuItems, a = r.symbolSize || 12;
                if (i.btnCount || (i.btnCount = 0), i.exportDivElements || (i.exportDivElements = [], i.exportSVGElements = []), !1 === r.enabled || !r.theme) return;
                let c = r.theme;
                i.styledMode || (c.fill = O(c.fill, "#ffffff"), c.stroke = O(c.stroke, "none")), s ? n = function (e) {
                    e && e.stopPropagation(), s.call(i, e)
                } : l && (n = function (e) {
                    e && e.stopPropagation(), i.contextMenu(p.menuClassName, l, p.translateX || 0, p.translateY || 0, p.width || 0, p.height || 0, p), p.setState(2)
                }), r.text && r.symbol ? c.paddingLeft = O(c.paddingLeft, 30) : r.text || w(c, {
                    width: r.width,
                    height: r.height,
                    padding: 0
                }), i.styledMode || (c["stroke-linecap"] = "round", c.fill = O(c.fill, "#ffffff"), c.stroke = O(c.stroke, "none"));
                let p = o.button(r.text, 0, 0, n, c, void 0, void 0, void 0, void 0, r.useHTML).addClass(e.className).attr({title: O(i.options.lang[r._titleKey || r.titleKey], "")});
                p.menuClassName = e.menuClassName || "highcharts-menu-" + i.btnCount++, r.symbol && (t = o.symbol(r.symbol, r.symbolX - a / 2, r.symbolY - a / 2, a, a, {
                    width: a,
                    height: a
                }).addClass("highcharts-button-symbol").attr({zIndex: 1}).add(p), i.styledMode || t.attr({
                    stroke: r.symbolStroke,
                    fill: r.symbolFill,
                    "stroke-width": r.symbolStrokeWidth || 1
                })), p.add(i.exportingGroup).align(w(r, {
                    width: p.width,
                    x: O(r.x, i.buttonOffset)
                }), !0, "spacingBox"), i.buttonOffset += ((p.width || 0) + r.buttonSpacing) * ("right" === r.align ? -1 : 1), i.exportSVGElements.push(p, t)
            }

            function H() {
                if (!this.printReverseInfo) return;
                let {childNodes: e, origDisplay: t, resetParams: n} = this.printReverseInfo;
                this.moveContainers(this.renderTo), [].forEach.call(e, function (e, n) {
                    1 === e.nodeType && (e.style.display = t[n] || "")
                }), this.isPrinting = !1, n && this.setSize.apply(this, n), delete this.printReverseInfo, i = void 0, C(this, "afterPrint")
            }

            function D() {
                let e = g.body, t = this.options.exporting.printMaxWidth,
                    n = {childNodes: e.childNodes, origDisplay: [], resetParams: void 0};
                this.isPrinting = !0, this.pointer.reset(null, 0), C(this, "beforePrint");
                let i = t && this.chartWidth > t;
                i && (n.resetParams = [this.options.chart.width, void 0, !1], this.setSize(t, void 0, !1)), [].forEach.call(n.childNodes, function (e, t) {
                    1 === e.nodeType && (n.origDisplay[t] = e.style.display, e.style.display = "none")
                }), this.moveContainers(e), this.printReverseInfo = n
            }

            function G(e) {
                e.renderExporting(), x(e, "redraw", e.renderExporting), x(e, "destroy", e.destroyExport)
            }

            function W(t, n, i, o, r, s, l) {
                let a = this, p = a.options.navigation, u = a.chartWidth, h = a.chartHeight, d = "cache-" + t,
                    f = Math.max(r, s), v, E = a[d];
                E || (a.exportContextMenu = a[d] = E = b("div", {className: t}, {
                    position: "absolute",
                    zIndex: 1e3,
                    padding: f + "px",
                    pointerEvents: "auto", ...a.renderer.style
                }, a.fixedDiv || a.container), v = b("ul", {className: "highcharts-menu"}, a.styledMode ? {} : {
                    listStyle: "none",
                    margin: 0,
                    padding: 0
                }, E), a.styledMode || y(v, w({
                    MozBoxShadow: "3px 3px 10px #888",
                    WebkitBoxShadow: "3px 3px 10px #888",
                    boxShadow: "3px 3px 10px #888"
                }, p.menuStyle)), E.hideMenu = function () {
                    y(E, {display: "none"}), l && l.setState(0), a.openMenu = !1, y(a.renderTo, {overflow: "hidden"}), y(a.container, {overflow: "hidden"}), c.clearTimeout(E.hideTimer), C(a, "exportMenuHidden")
                }, a.exportEvents.push(x(E, "mouseleave", function () {
                    E.hideTimer = m.setTimeout(E.hideMenu, 500)
                }), x(E, "mouseenter", function () {
                    c.clearTimeout(E.hideTimer)
                }), x(g, "mouseup", function (e) {
                    a.pointer.inClass(e.target, t) || E.hideMenu()
                }), x(E, "click", function () {
                    a.openMenu && E.hideMenu()
                })), n.forEach(function (t) {
                    if ("string" == typeof t && (t = a.options.exporting.menuItemDefinitions[t]), S(t, !0)) {
                        let n;
                        t.separator ? n = b("hr", void 0, void 0, v) : ("viewData" === t.textKey && a.isDataTableVisible && (t.textKey = "hideData"), n = b("li", {
                            className: "highcharts-menu-item",
                            onclick: function (e) {
                                e && e.stopPropagation(), E.hideMenu(), "string" != typeof t && t.onclick && t.onclick.apply(a, arguments)
                            }
                        }, void 0, v), e.setElementHTML(n, t.text || a.options.lang[t.textKey]), a.styledMode || (n.onmouseover = function () {
                            y(this, p.menuItemHoverStyle)
                        }, n.onmouseout = function () {
                            y(this, p.menuItemStyle)
                        }, y(n, w({cursor: "pointer"}, p.menuItemStyle || {})))), a.exportDivElements.push(n)
                    }
                }), a.exportDivElements.push(v, E), a.exportMenuWidth = E.offsetWidth, a.exportMenuHeight = E.offsetHeight);
                let T = {display: "block"};
                i + a.exportMenuWidth > u ? T.right = u - i - r - f + "px" : T.left = i - f + "px", o + s + a.exportMenuHeight > h && "top" !== l.alignOptions.verticalAlign ? T.bottom = h - o - f + "px" : T.top = o + s - f + "px", y(E, T), y(a.renderTo, {overflow: ""}), y(a.container, {overflow: ""}), a.openMenu = !0, C(a, "exportMenuShown")
            }

            function I(e) {
                let t;
                let n = e ? e.target : this, i = n.exportSVGElements, o = n.exportDivElements, r = n.exportEvents;
                i && (i.forEach((e, o) => {
                    e && (e.onclick = e.ontouchstart = null, n[t = "cache-" + e.menuClassName] && delete n[t], i[o] = e.destroy())
                }), i.length = 0), n.exportingGroup && (n.exportingGroup.destroy(), delete n.exportingGroup), o && (o.forEach(function (e, t) {
                    e && (c.clearTimeout(e.hideTimer), M(e, "mouseleave"), o[t] = e.onmouseout = e.onmouseover = e.ontouchstart = e.onclick = null, v(e))
                }), o.length = 0), r && (r.forEach(function (e) {
                    e()
                }), r.length = 0)
            }

            function R(e, t) {
                let n = this.getSVGForExport(e, t);
                e = T(this.options.exporting, e), a.post(e.url, {
                    filename: e.filename ? e.filename.replace(/\//g, "-") : this.getFilename(),
                    type: e.type,
                    width: e.width,
                    scale: e.scale,
                    svg: n
                }, e.fetchOptions)
            }

            function L() {
                return this.styledMode && this.inlineStyles(), this.container.innerHTML
            }

            function $() {
                let e = this.userOptions.title && this.userOptions.title.text, t = this.options.exporting.filename;
                return t ? t.replace(/\//g, "-") : ("string" == typeof e && (t = e.toLowerCase().replace(/<\/?[^>]+(>|$)/g, "").replace(/[\s_]+/g, "-").replace(/[^a-z0-9\-]/g, "").replace(/^[\-]+/g, "").replace(/[\-]+/g, "-").substr(0, 24).replace(/[\-]+$/g, "")), (!t || t.length < 5) && (t = "chart"), t)
            }

            function q(e) {
                let t, n, i = T(this.options, e);
                i.plotOptions = T(this.userOptions.plotOptions, e && e.plotOptions), i.time = T(this.userOptions.time, e && e.time);
                let o = b("div", null, {
                        position: "absolute",
                        top: "-9999em",
                        width: this.chartWidth + "px",
                        height: this.chartHeight + "px"
                    }, g.body), r = this.renderTo.style.width, s = this.renderTo.style.height,
                    l = i.exporting.sourceWidth || i.chart.width || /px$/.test(r) && parseInt(r, 10) || (i.isGantt ? 800 : 600),
                    a = i.exporting.sourceHeight || i.chart.height || /px$/.test(s) && parseInt(s, 10) || 400;
                w(i.chart, {
                    animation: !1,
                    renderTo: o,
                    forExport: !0,
                    renderer: "SVGRenderer",
                    width: l,
                    height: a
                }), i.exporting.enabled = !1, delete i.data, i.series = [], this.series.forEach(function (e) {
                    (n = T(e.userOptions, {
                        animation: !1,
                        enableMouseTracking: !1,
                        showCheckbox: !1,
                        visible: e.visible
                    })).isInternal || i.series.push(n)
                });
                let c = {};
                this.axes.forEach(function (e) {
                    e.userOptions.internalKey || (e.userOptions.internalKey = P()), e.options.isInternal || (c[e.coll] || (c[e.coll] = !0, i[e.coll] = []), i[e.coll].push(T(e.userOptions, {visible: e.visible})))
                }), i.colorAxis = this.userOptions.colorAxis;
                let p = new this.constructor(i, this.callback);
                return e && ["xAxis", "yAxis", "series"].forEach(function (t) {
                    let n = {};
                    e[t] && (n[t] = e[t], p.update(n))
                }), this.axes.forEach(function (e) {
                    let t = E(p.axes, function (t) {
                        return t.options.internalKey === e.userOptions.internalKey
                    }), n = e.getExtremes(), i = n.userMin, o = n.userMax;
                    t && (void 0 !== i && i !== t.min || void 0 !== o && o !== t.max) && t.setExtremes(i, o, !0, !1)
                }), t = p.getChartHTML(), C(this, "getSVG", {chartCopy: p}), t = this.sanitizeSVG(t, i), i = null, p.destroy(), v(o), t
            }

            function z(e, t) {
                let n = this.options.exporting;
                return this.getSVG(T({chart: {borderRadius: 0}}, n.chartOptions, t, {
                    exporting: {
                        sourceWidth: e && e.sourceWidth || n.sourceWidth,
                        sourceHeight: e && e.sourceHeight || n.sourceHeight
                    }
                }))
            }

            function V() {
                let e;
                let n = t.inlineAllowlist, i = {}, o = g.createElement("iframe");
                y(o, {width: "1px", height: "1px", visibility: "hidden"}), g.body.appendChild(o);
                let r = o.contentWindow && o.contentWindow.document;
                r && r.body.appendChild(r.createElementNS(f, "svg")), function t(o) {
                    let s, a, c, u, d, g;
                    let f = {};
                    if (r && 1 === o.nodeType && -1 === N.indexOf(o.nodeName)) {
                        if (s = m.getComputedStyle(o, null), a = "svg" === o.nodeName ? {} : m.getComputedStyle(o.parentNode, null), !i[o.nodeName]) {
                            e = r.getElementsByTagName("svg")[0], c = r.createElementNS(o.namespaceURI, o.nodeName), e.appendChild(c);
                            let t = m.getComputedStyle(c, null), n = {};
                            for (let e in t) "string" != typeof t[e] || /^[0-9]+$/.test(e) || (n[e] = t[e]);
                            i[o.nodeName] = n, "text" === o.nodeName && delete i.text.fill, e.removeChild(c)
                        }
                        for (let e in s) (l.isFirefox || l.isMS || l.isSafari || Object.hasOwnProperty.call(s, e)) && function (e, t) {
                            if (u = d = !1, n.length) {
                                for (g = n.length; g-- && !d;) d = n[g].test(t);
                                u = !d
                            }
                            for ("transform" === t && "none" === e && (u = !0), g = p.length; g-- && !u;) u = p[g].test(t) || "function" == typeof e;
                            !u && (a[t] !== e || "svg" === o.nodeName) && i[o.nodeName][t] !== e && (h && -1 === h.indexOf(t) ? f[t] = e : e && o.setAttribute(t.replace(/([A-Z])/g, function (e, t) {
                                return "-" + t.toLowerCase()
                            }), e))
                        }(s[e], e);
                        if (y(o, f), "svg" === o.nodeName && o.setAttribute("stroke-width", "1px"), "text" === o.nodeName) return;
                        [].forEach.call(o.children || o.childNodes, t)
                    }
                }(this.container.querySelector("svg")), e.parentNode.removeChild(e), o.parentNode.removeChild(o)
            }

            function K(e) {
                (this.fixedDiv ? [this.fixedDiv, this.scrollingContainer] : [this.container]).forEach(function (t) {
                    e.appendChild(t)
                })
            }

            function A() {
                let e = this, t = (t, n, i) => {
                    e.isDirtyExporting = !0, T(!0, e.options[t], n), O(i, !0) && e.redraw()
                };
                e.exporting = {
                    update: function (e, n) {
                        t("exporting", e, n)
                    }
                }, n.compose(e).navigation.addUpdate((e, n) => {
                    t("navigation", e, n)
                })
            }

            function B() {
                let e = this;
                e.isPrinting || (i = e, l.isSafari || e.beforePrint(), setTimeout(() => {
                    m.focus(), m.print(), l.isSafari || setTimeout(() => {
                        e.afterPrint()
                    }, 1e3)
                }, 1))
            }

            function U() {
                let e = this, t = e.options.exporting, n = t.buttons, i = e.isDirtyExporting || !e.exportSVGElements;
                e.buttonOffset = 0, e.isDirtyExporting && e.destroyExport(), i && !1 !== t.enabled && (e.exportEvents = [], e.exportingGroup = e.exportingGroup || e.renderer.g("exporting-group").attr({zIndex: 3}).add(), F(n, function (t) {
                    e.addButton(t)
                }), e.isDirtyExporting = !1)
            }

            function J(e, t) {
                let n = e.indexOf("</svg>") + 6, i = e.substr(n);
                return e = e.substr(0, n), t && t.exporting && t.exporting.allowHTML && i && (i = '<foreignObject x="0" y="0" width="' + t.chart.width + '" height="' + t.chart.height + '"><body xmlns="http://www.w3.org/1999/xhtml">' + i.replace(/(<(?:img|br).*?(?=\>))>/g, "$1 />") + "</body></foreignObject>", e = e.replace("</svg>", i + "</svg>")), e = e.replace(/zIndex="[^"]+"/g, "").replace(/symbolName="[^"]+"/g, "").replace(/jQuery[0-9]+="[^"]+"/g, "").replace(/url\(("|&quot;)(.*?)("|&quot;)\;?\)/g, "url($2)").replace(/url\([^#]+#/g, "url(#").replace(/<svg /, '<svg xmlns:xlink="http://www.w3.org/1999/xlink" ').replace(/ (|NS[0-9]+\:)href=/g, " xlink:href=").replace(/\n/, " ").replace(/(fill|stroke)="rgba\(([ 0-9]+,[ 0-9]+,[ 0-9]+),([ 0-9\.]+)\)"/g, '$1="rgb($2)" $1-opacity="$3"').replace(/&nbsp;/g, "\xa0").replace(/&shy;/g, "\xad")
            }

            t.compose = function e(t, n) {
                if (r.compose(n), s.compose(t), k(d, e)) {
                    let e = t.prototype;
                    e.afterPrint = H, e.exportChart = R, e.inlineStyles = V, e.print = B, e.sanitizeSVG = J, e.getChartHTML = L, e.getSVG = q, e.getSVGForExport = z, e.getFilename = $, e.moveContainers = K, e.beforePrint = D, e.contextMenu = W, e.addButton = j, e.destroyExport = I, e.renderExporting = U, e.callbacks.push(G), x(t, "init", A), l.isSafari && m.matchMedia("print").addListener(function (e) {
                        i && (e.matches ? i.beforePrint() : i.afterPrint())
                    }), u.exporting = T(o.exporting, u.exporting), u.lang = T(o.lang, u.lang), u.navigation = T(o.navigation, u.navigation)
                }
            }
        }(p || (p = {})), p
    }), n(t, "masters/modules/exporting.src.js", [t["Core/Globals.js"], t["Extensions/Exporting/Exporting.js"], t["Core/HttpUtilities.js"]], function (e, t, n) {
        e.HttpUtilities = n, e.ajax = n.ajax, e.getJSON = n.getJSON, e.post = n.post, t.compose(e.Chart, e.Renderer)
    })
});