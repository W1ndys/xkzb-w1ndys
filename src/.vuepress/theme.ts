import { hopeTheme } from "vuepress-theme-hope";

import navbar from "./navbar.js";
import sidebar from "./sidebar.js";

export default hopeTheme({
  hostname: "https://easy-qfnu.top",
  darkmode: "switch",
  author: {
    name: "W1ndys",
    url: "https://github.com/W1ndys",
  },

  logo: "./ezqf.svg",
  docsRepo: "W1ndys/Easy-QFNU",
  docsDir: "src",
  docsBranch: "main",
  repo: "W1ndys/Easy-QFNU",
  repoLabel: "GitHub",
  repoDisplay: true,

  // 导航栏
  navbar,
  // 侧边栏
  sidebar,
  // 页脚
  footer: "Easy-QFNU，让你的QFNU更简单~",
  copyright: "Copyright © 2024-2025 W1ndys",
  license: "MIT",
  displayFooter: true,
  // 加密配置
  encrypt: {
    config: {
      "/demo/encrypt.html": ["1234"],
    },
  },
  // 导航栏布局
  navbarLayout: {
    start: ["Brand"],
    center: ["Links"],
    end: ["Repo", "Outlook", "Search"],
  },
  // 打印
  print: true,
  // 全屏
  fullscreen: true,
  // 是否开启沉浸模式
  focus: false,
  // 是否开启纯净模式
  pure: false,
  // 如果想要实时查看任何改变，启用它。注: 这对更新性能有很大负面影响
  hotReload: true,
  // 主题Markdown选项
  markdown: {
    // 数学公式
    math: {
      type: "mathjax", // 或 'mathjax'
      output: "svg",
    },
    // 启用脚注
    footnote: true,
    // 启用下角标
    sub: true,
    // 启用上角标
    sup: true,
    // 选项卡
    tabs: true,
    // 任务列表
    tasklist: true,
    // 代码块
    vPre: true,
    // 对齐
    align: true,
    // 属性
    attrs: true,
    // 代码块标签
    codeTabs: true,
    // 组件
    component: true,
    // 演示
    demo: true,
    // 图片
    figure: true,
    // 图片懒加载
    imgLazyload: true,
    // 图片大小
    imgSize: true,
    // 包含
    include: true,
    // 标记
    mark: true,
    // 流程图
    plantuml: true,
    // 隐藏
    spoiler: true,
    // 自定义样式
    stylize: [
      {
        matcher: "Recommended",
        replacer: ({ tag }) => {
          if (tag === "em")
            return {
              tag: "Badge",
              attrs: { type: "tip" },
              content: "Recommended",
            };
        },
      },
    ],
    // 在启用之前安装 chart.js
    // chart: true,
    // insert component easily
    // 在启用之前安装 echarts
    // echarts: true,
    // 在启用之前安装 flowchart.ts
    // flowchart: true,
    // gfm requires mathjax-full to provide tex support
    // gfm: true,
    // 在启用之前安装 katex
    // katex: true,
    // 在启用之前安装 mathjax-full
    // mathjax: true,
    // 在启用之前安装 mermaid
    // mermaid: true,
    // playground: {
    //   presets: ["ts", "vue"],
    // },
    // 在启用之前安装 reveal.js
    // revealJs: {
    //   plugins: ["highlight", "math", "search", "notes", "zoom"],
    // },
    // 在启用之前安装 @vue/repl
    // vuePlayground: true,
    // install sandpack-vue3 before enabling it
    // sandpack: true,
  },
  // 在这里配置主题提供的插件

  plugins: {
    // 评论
    comment: {
      provider: "Waline",
      serverURL: "https://comments.easy-qfnu.top",
      pageview: true,
      pageSize: 10,
      // provider: "Giscus",
      // repo: "W1ndys/Easy-QFNU",
      // repoId: "R_kgDOLOtv9Q",
      // category: "Show and tell",
      // categoryId: "DIC_kwDOLOtv9c4Cd0Rh",
    },
    // 通知
    notice: {
      config: [
        {
          showOnce: true,
          // fullscreen: true,
          // confirm: true,
          path: "/EasySelectCourse",
          title: "解锁密码",
          content: "解锁密码请关注微信公众号【W1ndys】获取",
          actions: [
            {
              text: "点我去关注",
              link: "https://pic1.zhimg.com/80/v2-a42b58d3c6fa27d3ebe03b7090a7cf63.jpeg",
              type: "primary",
            },
            {
              text: "联系作者",
              link: "https://qm.qq.com/q/HlOWmsUlCQ",
              type: "primary",
            },
          ],
        },
      ],
    },
    // 版权
    copyright: {
      global: true,
      disableCopy: false,
      disableSelection: false,
      triggerLength: 50,
    },
    // 水印
    watermark: {
      enabled: true,
      watermarkOptions: {
        content: "微信公众号：W1ndys",
      },
    },
    // 搜索
    slimsearch: true,
    // 图标
    icon: {
      assets: "fontawesome",
    },

    // 组件
    components: {
      components: ["Badge", "VPCard"],
    },
    // 返回顶部
    backToTop: {
      /**
       * 显示返回顶部按钮的滚动阈值距离（以像素为单位）
       *
       * @default 100
       */
      threshold: 500,
      /**
       * 是否显示滚动进度
       *
       * @default true
       */
      progress: true,
    },

    // 如果你需要 PWA。安装 @vuepress/plugin-pwa 并取消下方注释
    // pwa: {
    //   favicon: "/favicon.ico",
    //   cacheHTML: true,
    //   cacheImage: true,
    //   appendBase: true,
    //   apple: {
    //     icon: "/assets/icon/apple-icon-152.png",
    //     statusBarColor: "black",
    //   },
    //   msTile: {
    //     image: "/assets/icon/ms-icon-144.png",
    //     color: "#ffffff",
    //   },
    //   manifest: {
    //     icons: [
    //       {
    //         src: "/assets/icon/chrome-mask-512.png",
    //         sizes: "512x512",
    //         purpose: "maskable",
    //         type: "image/png",
    //       },
    //       {
    //         src: "/assets/icon/chrome-mask-192.png",
    //         sizes: "192x192",
    //         purpose: "maskable",
    //         type: "image/png",
    //       },
    //       {
    //         src: "/assets/icon/chrome-512.png",
    //         sizes: "512x512",
    //         type: "image/png",
    //       },
    //       {
    //         src: "/assets/icon/chrome-192.png",
    //         sizes: "192x192",
    //         type: "image/png",
    //       },
    //     ],
    //     shortcuts: [
    //       {
    //         name: "Demo",
    //         short_name: "Demo",
    //         url: "/demo/",
    //         icons: [
    //           {
    //             src: "/assets/icon/guide-maskable.png",
    //             sizes: "192x192",
    //             purpose: "maskable",
    //             type: "image/png",
    //           },
    //         ],
    //       },
    //     ],
    //   },
    // },
  },
});
