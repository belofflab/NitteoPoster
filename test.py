from bs4 import BeautifulSoup

html = """
<div class="wootdaeteblock">
                        <div class="wotdtitle">Отдаете</div>
                                                <div class="wotdscom">(С учетом комиссии платежной системы Bitcoin)</div>
                                                <span class="wotdsumm">0.0126</span> <span class="wotdvtype">Bitcoin BTC</span><br>

                                                                                                        <span class="wotdcshet">Со счета</span> 1231232                                      </div>
                                <div class="wootdaeteblock">
                        <div class="wotdtitle">Получаете</div>
                                                <div class="wotdscom">(С учетом комиссии платежной системы Сбербанк)</div>
                                                <span class="wotdsumm">19954.368</span> <span class="wotdvtype">Сбербанк RUB</span><br>

                                                                                                        <span class="wotdcshet">На карту</span> 2202 2036 5757 2090
                                </div>

                                <div class="woveddann">
                                        <div class="wotdtitle">Личные данные</div>

                                                <div class="stepline"><span class="step2name">Имя:</span> Администратор</div>

                                                <div class="stepline"><span class="step2name">E-mail:</span> sadsad@mail.ru</div>

                                                <div class="stepline"><span class="step2name">Телефон:</span> 819938848281</div>
                                                                                </div>

                                <div class="wodpred">
                                        Использование сервиса после нажатия кнопки «Создать заявку» означает, что вы принимаете все основные требования, предъявляемые к Пользователю сервиса.</div>

                                <div class="wotdtext">
                                        <div class="wotdtextvn">
                                                <div class="checkbox act" id="check_rule_step"><input type="checkbox" id="createzajatos" name="" value="1"> С <a href="https://gogo.exchange/mobile.html?temp=tos">правилами сервиса</a> ознакомлен и согласен</div>
                                        </div>
                                </div>

                                <div class="inlinec hiden" style="display: block;">
                                        <input type="submit" formtarget="_top" name="" id="createzaja" value="Создать заявку">
                                </div>

                                <div class="resultgo"></div>

"""

soup = BeautifulSoup(html, 'lxml')

print("".join([i.text for i in soup.select('div.wootdaeteblock')]))