const express = require("express");
const app = express();

app.use(express.json());

app.post("/api/webhook", (req, res) => {
    console.log("收到 LINE Bot 訊息:", req.body);
    res.status(200).send("OK");
});

// 這行只適用於本地端測試，Vercel 部署後不需要
app.listen(3000, () => console.log("Webhook 伺服器運行中..."));