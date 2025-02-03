import { defineUserConfig } from "vuepress";

import theme from "./theme.js";

export default defineUserConfig({
  base: "/",
  lang: "zh-CN",
  title: "Easy-QFNU",
  description:
    "【Easy-QFNU】让你的QFNU更简单。免费、开源、共建、共享的公益项目，弥补你的信息差，帮助你更快地找到所需信息，致力于解决你在 QFNU 可能遇到的各种问题。",

  theme,
  head: [
    [
      "script",
      {
        charset: "UTF-8",
        id: "LA_COLLECT",
        src: "//sdk.51.la/js-sdk-pro.min.js",
      },
    ],
    [
      "script",
      {},
      "LA.init({id:'3HxQRMoHKBJizCgs',ck:'3HxQRMoHKBJizCgs',autoTrack:true,hashMode:true,screenRecord:true})",
    ],
  ],
  // 和 PWA 一起启用
  // shouldPrefetch: false,
});
