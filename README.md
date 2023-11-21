<h2>Регистрация в сервисах Google и установка библиотек</h2><br>
Для работы с таблицами нужно зарегистрироваться на Google, настроить проект и установить необходимые библиотеки.<br>
<br>
<a href="https://developers.google.com/sheets/">Официальная документация на английском языке находится здесь</a>.<br>
<br>
Сначала нужно зарегистрироваться на gmail.com (это вы можете сделать самостоятельно). Потом нужно создать проект (так Google предоставляет доступ к своим сервисам).<br>
<br>
Для этого зайдите на страницу <a href="https://console.developers.google.com/cloud-resource-manager">console.developers.google.com/cloud-resource-manager</a> и нажать «Создать проект»<br>
<br>
<img src="images/s1.png"><br>
<br>
Введите имя проекта и нажмите «Создать»<br>
<br>
<img src="images/s2.png"><br>
<br>
В обновленном списке проектов зайдите в меню «Настройки», затем «IAM»<br>
<img src="images/s3.png"><br>
<img src="images/s4.png"><br>
<br>
В открывшемся окне нажмите «Добавить», внесите свой email с домена gmail.com и выберите группу «Проект» — «Владелец»<br>
<br>
<img src="images/s5.png"><br>
<img src="images/s6.png"><br>
<br>
Сохраните изменения.<br>
<br>
Снова зайдите на страницу <a href="https://console.developers.google.com/cloud-resource-manager">console.developers.google.com/cloud-resource-manager</a><br>
<br>
Выберите на своем проекте меню «Настройки»<br>
<br>
<img src="images/s3.png"><br>
В открывшемся окне выберите «Сервисные аккаунты», а затем «Создать сервисный аккаунт»<br>
<br>
<img src="images/s7.png"><br>
Введите название аккаунта и нажмите «Создать»<br>
<br>
<img src="images/s8.png"><br>
Выберите роль «Владелец» и нажмите «Продолжить»<br>
<br>
<img src="images/s9.png"><br>
В появившемся окне нажмите «Создать ключ»<br>
<br>
<img src="images/s10.png"><br>
<img src="images/s11.png"><br>
<img src="images/s12.png"><br>
Выберите тип ключа «json» и нажмите «Создать»<br>
<br>
Будет создан и сразу же скачан файл с ключами. Сохраните его, именно благодаря ему мы сможем получать доступ к сервисам Google.<br>
<br>
Нажмите на кнопку с тремя горизонтальными штрихами, слева от надписи «Google APIs», выберите пункт «API и сервисы», а в нем подпункт «Панель управления».<br>
<br>
<img src="https://habrastorage.org/r/w1560/webt/n9/0c/gh/n90cgh2hyrqigsxjus02cwhrt-c.jpeg" data-src="https://habrastorage.org/webt/n9/0c/gh/n90cgh2hyrqigsxjus02cwhrt-c.jpeg"><br>
<br>
В открывшемся окне нажмите «Включить API и сервисы»<br>
<br>
<img src="https://habrastorage.org/r/w1560/webt/w8/3f/wc/w83fwcm2h2zcq4qza3pysyjhseu.jpeg" data-src="https://habrastorage.org/webt/w8/3f/wc/w83fwcm2h2zcq4qza3pysyjhseu.jpeg"><br>
<br>
Введите в строку поиска «google drive» и кликните на сервисе «Google Drive API»<br>
<br>
<img src="https://habrastorage.org/r/w1560/webt/fj/ks/iw/fjksiwvxazgd-6erfruqwrwq8os.jpeg" data-src="https://habrastorage.org/webt/fj/ks/iw/fjksiwvxazgd-6erfruqwrwq8os.jpeg"><br>
<br>
Нажмите «Включить»<br>
<br>
<img src="https://habrastorage.org/r/w1560/webt/jk/f-/ys/jkf-ysfiu--oqojyf8vi1lwphao.jpeg" data-src="https://habrastorage.org/webt/jk/f-/ys/jkf-ysfiu--oqojyf8vi1lwphao.jpeg"><br>
<br>
Сайт уведомит вас, что API включено и предупредит, что нужно создать учетные данные. Игнорируйте это предупреждение (ведь мы уже создали сервисный аккаунт).<br>
<br>
<img src="https://habrastorage.org/r/w1560/webt/se/e4/z4/see4z4tacpn3manmkn_tixgkgck.jpeg" data-src="https://habrastorage.org/webt/se/e4/z4/see4z4tacpn3manmkn_tixgkgck.jpeg"><br>
<br>
Снова заходите в панель управления<br>
<br>
<img src="https://habrastorage.org/r/w1560/webt/c0/ak/ln/c0aklnjxew9zwlph6fgp1ym-yt8.jpeg" data-src="https://habrastorage.org/webt/c0/ak/ln/c0aklnjxew9zwlph6fgp1ym-yt8.jpeg"><br>
<br>
В открывшемся окне нажмите «Включить API и сервисы»<br>
<br>
<img src="https://habrastorage.org/r/w1560/webt/w8/3f/wc/w83fwcm2h2zcq4qza3pysyjhseu.jpeg" data-src="https://habrastorage.org/webt/w8/3f/wc/w83fwcm2h2zcq4qza3pysyjhseu.jpeg"><br>
<br>
Введите в строку поиска «sheet» и кликните на сервисе «Google Sheets API»<br>
<br>
<img src="null" data-src="http://img/Task09_17.jpg" alt="Изображение не загружено"><br>
<br>
Убедитесь, что это API подключено. Оно должно включиться автоматически, при подключении Google Drive API. Если оно подключено, вы увидите кнопку «Управление API», если нет — кнопку «Включить». Включите его, при необходимости.<br>
<br>
Все остальное в файлах <code>shower.py</code> и <code>async_.py</code>
