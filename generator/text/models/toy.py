class EnToyTextGenModel(object):
    def __init__(self):
        self.text = [
            "A kitten walks on the road", "meets a little pig", "meets a lamb"   
        ]

        # self.text = [
        #     '一只小猫在马路上','遇到一只小狗','遇到一只小羊'
        # ]
        
    def run(self,input_text):
        resp = {
            'lang':'en',
            'out_text':[]
        }
        for t in self.text:
            resp['out_text'].append({
                'en':t,
            })
        return resp

class ZhToyTextGenModel(object):
    def __init__(self):
        self.text =['小孩子养宠物', '可以更好地提升小孩子的责任感和独立感', '但也要慎重的选择合适的宠物', '因为只有经过一定的训练养成',
                    '它们才能够成长起 来', '一起玩耍和度过一段欢快的时光', '宠物不仅能够陪伴小孩子渡过寂寞时光', '还能培养小孩子处事冷静、自信以及情感交流和沟通能力', '在养宠物的过程中', '小孩子们可以唤醒和发掘他们被磨练出来的坚毅和耐力',
                    '能够亲身体验到勤勉 和坚持的重要性']
        
        self.en_text =  ['Children have pets.', "It can better enhance children's sense of responsibility and independence.", 'But also choose the suitable pet carefully.', 'Only through certain training and cultivation.', 'They can only grow.', 'Have fun and enjoy a pleasant time together.', 
                         'Pets can not only accompany children to pass the lonely time.', 'It can also cultivate children to be calm, confident in their dealings, and with the ability of emotional communication and communication.', 'During the process of keeping pets', 
                         'Children can awaken and tap into the strength and endurance they have forged.', 'Being able to experience the importance of diligence and persistence in person.']
    def run(self,input_text):
        resp = {
            'lang':'zh',
            'out_text':[]
        }
        for en_t,zh_t in zip(self.en_text,self.text):
            resp['out_text'].append({
                'en':en_t,
                'zh':zh_t,
            })
        return resp
    
    
class ZhToyURL2TextModel(object):
    def __init__(self):
        self.text =['美国短毛猫', '是一种神奇又魔幻的宠物猫品种', '短毛猫们优雅可爱', '活力无比', 
                    '能拥有多达80多种头毛色彩', '最出名的是银虎斑', '其银色毛发中透着浓厚的黑色斑纹', 
                    '除此之外', '它们还非常温柔', '是非常适合家庭和人类相处的宠物',
                    '并且平均寿命达15-20年', '这种可爱的猫品种', '正在受到越来越多人的喜爱',
                    '不妨试试你也来养一只吧']
        
        self.en_text =  ['American shorthair cats', 'It is a pet cat breed that is both magical and magical.',
                         'horthair cats are elegant and adorable.', 
                         'horthair cats have incredible amount of energy.', 'horthair cats can have up to over 80 hair color variations.',
                         'The most famous one is the Silver Tiger.',
                         '.There are thick black stripes in shorthair cats’ silver hair.', 
                         'Apart from this2In addition to this.', 'shorthair cats are also very gentle.', 
                         'It is a very suitable pet for families and for humans to interact with.',
                         '.Life expectancy averages from 15-20 years.', 'This adorable breed of cats.', 
                         'Being increasingly loved by more and more people.', 'Why not give it a try and take care of one?']
    def run(self,input_text):
        resp = {
            'lang':'zh',
            'out_text':[]
        }
        for en_t,zh_t in zip(self.en_text,self.text):
            resp['out_text'].append({
                'en':en_t,
                'zh':zh_t,
            })
        return resp