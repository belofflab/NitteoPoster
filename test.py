# import requests

# from bs4 import BeautifulSoup

# # a = "https://gogo.exchange/server/api/v1/send_message"
# # requests.post(url='http://194.87.62.91:8005/api/v1/send_message', json={'res': 1})
# # requests.post(url='https://kumicho.pw/api/v1/send_message', json={'res': 1})

# html = """\n\t\t\t
# <div class="xchangestep2bodyvn">
# \t\t\t\n\t\t\n\t\t\t<div class="stepblock">
# \n\t\t\t\t<div class="steptitle">Отдаете <span class="steptitlemin">С учетом комиссии платежной системы <b>Bitcoin</b></span>
# </div>\n\t\t\t\t<div class="stepblleft">\n\t\t\t\t\n\t\t\t\t\t<p><span class="steptitsumm">Сумма:</span> 
# <b>0.1389</b> <span class="steptitvtype">Bitcoin BTC</span></p>\n\t\t\t\t\t<p><span class="steptitsumm">Со счета:</span>
#  <b>1231232</b></p>\n\t\t\t\t</div>\n\t\t\t\t<div class="stepblright">\n\t\t\t\t\t<div class="stepicotext">Bitcoin BTC</div>
#  \n\t\t\t\t\t<div class="stepico" style="background: url(/wp-content/uploads/coins/bitcoin.svg) no-repeat center center;">
#  </div>\n\t\t\t\t\t\t<div class="clear"></div>\n\t\t\t\t</div>\n\t\t\t\t\t<div class="clear"></div>\n\t\t\t</div>\n\t\t\t\n\t\t\t
#  <div class="stepblock">\n\t\t\t\t<div class="steptitle">Получаете <span class="steptitlemin">
#  С учетом комиссии платежной системы <b>Сбербанк</b></span></div>\n\t\t\t\t<div class="stepblleft">\n\t\t\t\t\t\n\t\t\t\t\t<p>
#  <span class="steptitsumm">Сумма:</span> <b>200004.556</b> <span class="steptitvtype">Сбербанк RUB</span></p>\n\t\t\t\t\t<p>
#  <span class="steptitsumm">На карту:</span> <b>2202 2036 5757 2090</b></p>\n\t\t\t\t</div>\n\t\t\t\t<div class="stepblright">\n\t\t\t\t\t
#  <div class="stepicotext">Сбербанк RUB</div>\n\t\t\t\t\t<div class="stepico" style="background: url(/wp-content/uploads/coins/sberbank.svg) 
#  no-repeat center center;"></div>\t\t\t\t\n\t\t\t\t\n\t\t\t\t\t<div class="clear"></div>\n\t\t\t\t</div>\t\t\t\t\n\t\t\t\t\t<div class="clear">
#  </div>\n\t\t\t</div>\n\t\t\t\n\t\t\t<div class="stepblock lichdann">\n\t\t\t\t<div class="steptitle">Личные данные</div>\n\t\t\t\t\n\t\t\t\t
#  <div class="lichdannvn">\n\t\t\t\t\n\t\t\t\t\t<div class="stepline"><span class="step2name">Имя:</span> Администратор</div>
#  \n\t\t\t\t\t\n\t\t\t\t\t<div class="stepline"><span class="step2name">E-mail:</span> sadsad@mail.ru</div>\n\t\t\t\t\n\t\t\t\t\t
#  <div class="stepline"><span class="step2name">Телефон:</span> 819938848281</div>\n\t\t\t\t\t\t\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t\t\n\t\t\t
#  <div class="stepcheckbox">\n\t\t        <div class="checkbox act" id="check_rule_step"><input type="checkbox" id="createzajatos" name="" value="1"> С <a href="https://gogo.exchange/tos/">правилами сервиса</a> ознакомлен и согласен</div>\n\t\t    </div>\n\t\t\t<div class="biginfo">\n\t\t\t    <div class="biginfovn">\n\t\t\t\t    <div class="binfotitle">Внимание!</div>\n\t\t\t\t    Использование сервиса после нажатия кнопки «Создать заявку» означает, что вы принимаете все основные требования, предъявляемые к Пользователю сервиса.\n\t\t\t    </div>\n\t\t\t</div>\n\t\t    <div class="stepwarning">Внимательно проверьте правильность платежных данных перед созданием заявки!</div>\n\t\t\t\n            <form action="https://gogo.exchange/ajax-createbids.html?meth=post&amp;yid=3f4d0ec5d934" class="ajax_post_form" method="post">\n\t\t\t\t<input type="hidden" name="hash" value="PrqHnbSsTsbEvXOJmgV22AYPufGlpEO4iGo">\n\t\t\t\t<div class="step2submit">\n\t\t            <input type="submit" name="" formtarget="_top" id="createzaja" value="Создать заявку">\n\t\t        </div>\n\n\t\t\t\t<div class="ajax_post_bids_res" style="padding: 10px 0px;">\n\t\t\t\t\t<div class="resultgo"></div>\n\t\t\t\t</div>\t\t\t\t\n            </form>\t\t\t\n\t\t\t\n\t\t\t</div>\n\t\t"""

# soup = BeautifulSoup(html, 'lxml')

# block = soup.select('div.stepblock')
# block_lk = soup.select_one('div.stepblock.lichdann')

# print(f"""
# {block[0].select_one('div.stepblleft').text}
# {block[1].select_one('div.steptitle').text}
# {block[1].select_one('div.stepblleft').text}
# {block_lk.text}
# """)

# a = """
# Отдаете С учетом комиссии платежной системы Bitcoin


# Сумма:
# 0.1389 Bitcoin BTC
# Со счета:
# 1231232

# Получаете
#  С учетом комиссии платежной системы Сбербанк


# Сумма: 200004.556 Сбербанк RUB

# На карту: 2202 2036 5757 2090


# Личные данные

# Имя: Администратор
# E-mail: sadsad@mail.ru
# Телефон: 819938848281
# """


l = [(1, 'USDT', 'RUB SBER', 'Binance.com (price) (USDT =&gt; RUB)', '1', '[binance_usdtrub] * 1,02', 7), (2, 'BTC', 'RUB', 'Binance.com (price) (BTC =&gt; RUB)', '1', '[binance_btcrub] * 1,01', 11), (3, 'RUB SBER', 'USDT', 'Binance.com (price) (RUB =&gt; USDT)', '[binance_usdtrub] * 1,05', '1', 8), (4, 'ETH', 'RUB (SBER)', 'Binance.com (price) (ETH =&gt; RUB (SBER))', '1', '[binance_ethrub]', 12), (5, 'RUB', 'BTC', 'Binance.com (price) (RUB =&gt; BTC)', '[binance_btcrub] * 1,055', '1', 13), (6, 'RUB', 'ETH', 'Binance.com (price) (RUB =&gt; ETH)', '[binance_ethrub] * 1,06', '1', 14), (7, 'CASH USD', 'USDT', 'CASH USD-&gt;USDT (ISTANBUL)', '1', '[binance_busdusdt] / 1,008', 15), (8, 'USDT', 'CASH USD', 'USDT-&gt;CASH USD (ISTANBUL)', '1', '[binance_busdusdt] * 1,002', 16), (9, 'USDT', 'CASH USD', 'USDT-&gt;CASH USD (ANTALYA)', '1', '[binance_busdusdt] * 1,00', 17), (10, 'CASH EUR', 'USDT', 'CASH EUR (BARCELONA) -&gt; USDT', '1', '[binance_eurusdt] / 1,053', 18), (11, 'CASH EUR', 'USDT', 'CASH EUR (VALENCIA) -&gt; USDT', '1', '[binance_eurusdt] / 1,053', 20), (12, 'CASH EUR', 'USDT', 'CASH EUR (MARBELLA) -&gt; USDT', '1', '[binance_eurusdt] / 1,053', 21), (13, 'USDT', 'CASH EUR', 'USDT-&gt;CASH EUR (BARCELONA)', '[binance_eurusdt] * 1,010', '1', 19), (14, 'USDT', 'CASH EUR', 'USDT-&gt;CASH EUR (MARBELLA)', '[binance_eurusdt] * 1,010', '1', 22), (15, 'USDT', 'CASH EUR', 'USDT-&gt;CASH EUR (VILNIUS)', '[binance_eurusdt] * 1,005', '1', 23), (16, 'USDT', 'CASH EUR', 'USDT-&gt;CASH EUR (WARSAW)', '[binance_eurusdt] * 1,005', '1', 25), (17, 'CASH EUR', 'USDT', 'CASH EUR (VILNIUS)-&gt; USDT', '1', '[binance_eurusdt] / 1,02', 24), (18, 'CASH EUR', 'USDT', 'CASH EUR (WASRSAW)-&gt; USDT', '1', '[binance_eurusdt] / 1,02', 26), (19, 'Сash RUB', 'USDT', 'Сash RUB -&gt; USDT (MOSCOW)', '[binance_usdtrub] * 1,05', '1', 9), (20, 'USDT', 'Cash RUB', 'USDT -&gt; Cash RUB (MOSCOW)', '1', '[binance_usdtrub] * 1,02', 10), (21, 'TRY', 'USDTTRC20', 'TRY - &gt; USDTTRC20', '[binance_usdttry] * 1,007', '1', 1), (22, 'USDTTRC20', 'TRY', 'USDTTRC20 - &gt; TRY', '1', '[binance_usdttry] / 1,02', 2), (23, 'RUB TINKOFF', 'USDT', 'TINKOFF RUB =&gt; USDT', '[binance_usdtrub] * 1,05', '1', 3), (24, 'USDT', 'TINKOFF RUB', 'USDT =&gt; TINKOFF RUB', '1', '[binance_usdtrub] * 1,02', 4), (25, 'Альфа Банк RUB', 'USDT', 'Альфа Банк RUB =&gt; USDT', '[binance_usdtrub] * 1,07', '1', 5), (26, 'USDT', 'Альфа Банк RUB', 'USDT =&gt; Альфа Банк RUB', '1', '[binance_usdtrub] * 1,02', 6)]


for el in l:
  print(el[1] if len(el[1].split(' ')) == 1  else el[1].split(' ')[-1] + ' -> ' + el[1] if len(el[2].split(' ')) == 1 else el[2].split(' ')[-1])