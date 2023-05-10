# Open Chat Video Editor
## 简介
Open Chat Video Editor是开源的短视频生成和编辑工具，整体技术框架如下：

![sys中文](https://user-images.githubusercontent.com/21036347/236475457-e6104baa-11c2-4fe9-88b3-f328114d0076.png)


## TODO 
- [x] **windows、linux不同系统更方便的install指引**
- [x] **创建docker，方便大家一键使用**
- [ ] **能够在线直接快速体验的url**
- [ ] 在短视频文案数据上对文本模型finetune,支持更多的文案风格
- [ ]  finetune SD模型，提升图像和视频的生成效果



目前具有以下特点：
- 1）**一键生成可用的短视频**，包括：配音、背景音乐、字幕等。

- 2）算法和数据均基于开源项目，方便技术交流和学习
- 3）支持多种输入数据，方便对各种各样的数据，一键转短视频，目前支持：
  -    [x] **短句转短视频**（Text2Video）: 根据输入的简短文字，生成短视频文案，并合成短视频
  -    [x] **网页链接转短视频**（Url2Video）: 自动对网页的内容进行提取，生成视频文案，并生成短视频
  -    [ ] **长视频转短视频**（Long Video to Short Video）: 对输入的长视频进行分析和摘要，并生成短视频
- 4）涵盖**生成模型**和**多模态检索模型**等多种主流算法和模型，如: Chatgpt,Stable Diffusion,CLIP 等

文本生成上，支持：
- [x] ChatGPT 
- [ ] BELLE
- [ ] Alpaca
- [ ] Dolly 
等多种模型

视觉信息生成上，支持图像和视频两种模态，生成方式上，支持检索和生成两种模型，目前共有6种模式：
- [x] 图像检索
- [x] 图像生成（stable diffusion）
- [x] 先图像检索，再基于stable diffusion 进行图像生成
- [x] 视频检索
- [ ] 视频生成（stable diffusion）
- [ ] 视频检索后，再基于stable diffusion 进行视频生成

## 结果展示 
### 1、短句转短视频（Text2Video）
界面如下:
![text2video](https://user-images.githubusercontent.com/21036347/236427963-7e9a166b-c085-4af8-b691-5a67f3e865e5.png)
以输入文案：【小孩子养宠物】为例，利用文本模型（如：chatgpt 等），可以自动生成一个较长的短视频文案：
```
['小孩子养宠物', '可以更好地提升小孩子的责任感和独立感', '但也要慎重的选择合适的宠物', '因为只有经过一定的训练养成', '它们才能够成长起来', '一起玩耍和度过一段欢快的时光', '宠物不仅能够陪伴小孩子渡过寂寞时光', '还能培养小孩子处事冷静、自信以及情感交流和沟通能力', '在养宠物的过程中', '小孩子们可以唤醒和发掘他们被磨练出来的坚毅和耐力', '能够亲身体验到勤勉 和坚持的重要性'] 
```

根据不同的视频生成模式，可以生成不同的视频，各个模式对比如下: 

 **1）图像检索** 

https://user-images.githubusercontent.com/21036347/236428839-9c3c3a2d-6163-4577-82f5-5815772f294f.mp4

**2）图像生成（stable diffusion）** 

https://user-images.githubusercontent.com/21036347/236429111-b151f3b5-64d0-4572-8daa-29a78a3d1f3d.mp4

**3）先图像检索，再基于stable diffusion 进行图像生成** 

https://user-images.githubusercontent.com/21036347/236429690-93ea7377-e233-4629-868f-ef953a4dfa4c.mp4

**4）视频检索** 

https://user-images.githubusercontent.com/21036347/236430102-6054b28c-ebeb-42a2-880e-b2656fc32138.mp4

### 2、网页转短视频（Url2Video）
界面如下：

![url2video](https://user-images.githubusercontent.com/21036347/236430693-fe9b3d15-8da8-4a50-b7a9-b4dc93614076.png)

1）输入一个url, 例如：https://zh.wikipedia.org/wiki/%E7%BE%8E%E5%9B%BD%E7%9F%AD%E6%AF%9B%E7%8C%AB
其内容是：美国短毛猫的维基百科

![wiki](https://user-images.githubusercontent.com/21036347/236431138-5fbb6cf2-07c8-41a3-989d-64731a6891d4.png)

2）解析网页并自动摘要成短视频文案，结果如下：
```
['\n\n美国短毛猫', '是一种神奇又魔幻的宠物猫品种', '它们优雅可爱', '活力无比', '能拥有多达80多种头毛色彩', '最出名的是银虎斑', '其银色毛发中透着浓厚的黑色斑 
纹', '除此之外', '它们还非常温柔', '是非常适合家庭和人类相处的宠物', '并且平均寿命达15-20年', '这种可爱的猫 
品种', '正在受到越来越多人的喜爱', '不妨试试你也来养一只吧']

```
3）自动合成短视频
例如图像生成模式下生成的结果如下，其他模式不再一一对比

https://user-images.githubusercontent.com/21036347/236431745-9f61ebcc-91b5-4157-adf9-abf9c371e461.mp4 

### 3、长视频转短视频（Long Video to Short Video）
  **即将发布，敬请期待**


## 安装与使用 
### 环境安装
根据不同需求，选择不同的安装方式1、2、和3、任选其一。
#### 1、Docker
目前docker环境因为每个人的cuda版本可能不一样，所以无法保证都能够正常使用GPU。目前仅支持图像检索模式，且占用比较多的储存（24G）。
```
docker pull iamjunhonghuang/open-chat-video-editor:retrival
docker run -it --network=host -v /YourPath/open-chat-video-editor:/YourPath/open-chat-video-editor/ iamjunhonghuang/open-chat-video-editor:retrival bash
conda activate open_editor
```
#### 2、Linux (目前仅在centOS测试)
1）首先安装基于conda的python环境，gcc版本安装测试时是8.5.0，所以尽量升级到8以上
```
conda env create -f env.yaml
conda env update -f env.yaml #假如第一行出现错误，需要更新使用的命令
```
2） 接着安装环境依赖，主要目的是正常安装ImageMagick，其他linux版本可以参考
```
# yum groupinstall 'Development Tools'
# yum install ghostscript
# yum -y install bzip2-devel freetype-devel libjpeg-devel libpng-devel libtiff-devel giflib-devel zlib-devel ghostscript-devel djvulibre-devel libwmf-devel jasper-devel libtool-ltdl-devel libX11-devel libXext-devel libXt-devel libxml2-devel librsvg2-devel OpenEXR-devel php-devel
# wget https://www.imagemagick.org/download/ImageMagick.tar.gz
# tar xvzf ImageMagick.tar.gz
# cd ImageMagick*
# ./configure
# make
# make install
```
3）需要修改moviepy的调用路径，也就是将下面文件
```
$HOME/anaconda3/envs/open_editor/lib/python3.8/site-packages/moviepy/config_defaults.py
```
修改成
      
```
#IMAGEMAGICK_BINARY = os.getenv('IMAGEMAGICK_BINARY', 'auto-detect')
IMAGEMAGICK_BINARY='/usr/local/bin/magick'
```
4）目前暂不支持中文字幕显示，所以需要修改配置文件yaml中的字体设置，例如’image_by_retrieval_text_by_chatgpt_zh.yaml‘
```
  subtitle:
    font: DejaVu-Sans-Bold-Oblique
    # font: Cantarell-Regular
    # font: 华文细黑
```


#### 3、Windows
1）建议使用python 3.8.16版本：
```
conda create -n open_editor python=3.8.16
```
2）安装pytorch 
```
# GPU 版本
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117

# CPU版本
pip3 install torch torchvision torchaudio

```

3）安装其他依赖环境

```pip install -r requirements.txt```

4）安装clip 

 ```pip install git+https://github.com/openai/CLIP.git```
 
4）安装faiss 

 ```conda install -c pytorch faiss-cpu```

### 代码执行
1）根据实际需要，选择不同的配置文件
|  配置文件   | 说明  |
|  ----  | ----  |
| configs/text2video/image_by_retrieval_text_by_chatgpt_zh.yaml  | 短文本转视频,视频文案采用chatgpt生成,视觉部分采用图像检索来生成|
| configs\text2video\image_by_diffusion_text_by_chatgpt_zh.yaml  | 短文本转视频,视频文案采用chatgpt生成, 视觉部分采用图像stable diffusion 来生成 |
| configs\text2video\image_by_retrieval_then_diffusion_chatgpt_zh.yaml |短文本转视频,视频文案采用chatgpt生成,视觉部分采用先图像检索，然后再基于图像的stable diffusion 来生成|
|configs\text2video\video_by_retrieval_text_by_chatgpt_zh.yaml|短文本转视频, 视频文案采用chatgpt生成,视觉部分采用视频检索来生成| 
| configs\url2video\image_by_retrieval_text_by_chatgpt.yaml | url转视频，视频文案采用chatgpt生成,视觉部分采用图像检索来生成|
| configs\url2video\image_by_diffusion_text_by_chatgpt.yaml|url转视频,视频文案采用chatgpt生成, 视觉部分采用图像stable diffusion 来生成|
|configs\url2video\image_by_retrieval_then_diffusion_chatgpt.yaml|url转视频,视频文案采用chatgpt生成,视觉部分采用先图像检索，然后再基于图像的stable diffusion 来生成|
|configs\url2video\video_by_retrieval_text_by_chatgpt.yaml|url转视频,视频文案采用chatgpt生成,视觉部分采用视频检索来生成 |


**需要注意的是：如果要采用ChatGPT来生成文案，需要在配置文件里面，添加organization 和 api_key**

2）下载数据索引和meta信息[data.tar](https://pan.quark.cn/s/19fa46ceb2cb),并解压到 data/index 目录下，

3）执行脚本 
```
# Text to video 
python  app/app.py --func Text2VideoEditor  --cfg ${cfg_file}


# URL to video 
python  app/app.py --func URL2VideoEditor  --cfg ${cfg_file}

```


## 声明 
1、数据来源 
图像检索数据来源于:[LAION-5B](https://laion.ai/blog/laion-5b/)

视频检索数据来源于：[webvid-10m](https://m-bain.github.io/webvid-dataset/)

请注意，我们并不拥有数据版权

2、该项目仅用于交流学习，不得用于商业，以及其他会对社会带来危害的用途。


## 交流与学习 
欢迎通过[Discard](https://discord.gg/yWt59JUd) 或者微信与我们交流学习

一群200人已满,

![微信图片_20230505204811](https://user-images.githubusercontent.com/21036347/236461673-53188ad6-ad27-470f-9910-6e648f92c240.jpg)

二群200人已满，

![WechatIMG1888](https://user-images.githubusercontent.com/21036347/236738826-ec47d75e-5b0d-45ad-8f09-8468e9eb8172.jpeg)

请加三群：

![301683610444_ pic](https://user-images.githubusercontent.com/26428693/237003622-af8b9c38-1d88-4518-8080-354666e7fa19.jpg)


