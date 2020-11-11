from googletrans import Translator

def back_translate(ch_txt):
    translator = Translator()
    while True:
        try:
            en = translator.translate(ch_txt, src='zh-CN').text
            while True:
                try:
                    back_trans_ch = translator.translate(en, dest='zh-CN').text
                    return back_trans_ch
                except Exception as e:
                    translator = Translator()

        except Exception as e:
            translator = Translator()




