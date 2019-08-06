# 用于生成验证码的微服务模块
Created by XinyaoTian

## 使用方法

启动该服务后，向该服务相应端口的 URI /api/captcha 发送 HTTP 的 GET 请求，
即可获取相应验证码的图像，并在 HTTP 头部(header)中寻找 'CAPTCHA' 字段，
可获取验证码图片内文字所对应的字符串。