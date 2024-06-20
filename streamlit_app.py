import streamlit as st 
import pandas as pd
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
from streamlit_echarts import st_echarts

html_content = """
<!DOCTYPE html>
<html>

<head>
  <title>AI營養建議師</title>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
  <link rel="stylesheet" href="{{ url_for('static', filename='html_p/assets/css/main.css') }}" />
  <noscript>
    <link rel="stylesheet" href="{{ url_for('static', filename='html_p/assets/css/noscript.css') }}" />
  </noscript>


</head>


<body class="is-preload">
  <div id="wrapper">
    <header id="header">
      <div class="logo">
        <span class="icon fa-gem"></span>
      </div>
      <div class="content">
        <div class="inner">
          <h1>AI營養建議師</h1>
          <p>根據自身狀況提供每日營養攝取建議...</p>
        </div>
      </div>
      <nav>
        <ul>
          <li><a href="#intro">介紹</a></li>
          <li><a href="#work">營養建議服務</a></li>
          <li><a href="#about">AI營養建議師</a></li>
          <li><a href="#contact">團隊</a></li>
        </ul>
      </nav>
    </header>

    <div id="main">
      <article id="intro">
        <h2 class="major">Intro</h2>
        <span class="image main"><img src="{{ url_for('static', filename='html_p/images/pic01.jpg') }}" alt="" /></span>
        <h3>每日所需熱量(kcal)</h3>
        <div>
          <canvas id="myChart"></canvas>
        </div>

        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

        <script>
          const ctx = document.getElementById('myChart');

          new Chart(ctx, {
            type: 'bar',
            data: {
              labels: ['女', '男'],
              datasets: [
                {
                  label: '13-15',
                  data: [2200, 2600],
                  backgroundColor: 'rgba(255, 99, 132, 0.1)',
                  borderColor: 'rgba(255, 99, 132, 1)',
                  borderWidth: 1
                },
                {
                  label: '16-18',
                  data: [2100, 2750],
                  backgroundColor: 'rgba(255, 159, 64, 0.1)',
                  borderColor: 'rgba(255, 159, 64, 1)',
                  borderWidth: 1
                },
                {
                  label: '19-30',
                  data: [1775, 2225],
                  backgroundColor: 'rgba(255, 205, 86, 0.1)',
                  borderColor: 'rgba(255, 205, 86, 1)',
                  borderWidth: 1
                },
                {
                  label: '31-50',
                  data: [1775, 2225],
                  backgroundColor: 'rgba(255, 192, 192, 0.1)',
                  borderColor: 'rgba(255, 192, 192, 1)',
                  borderWidth: 1
                },
                {
                  label: '51-70',
                  data: [1700, 2100],
                  backgroundColor: 'rgba(255, 162, 235, 0.1)',
                  borderColor: 'rgba(255, 162, 235, 1)',
                  borderWidth: 1
                },
                {
                  label: '71-',
                  data: [1500, 1900],
                  backgroundColor: 'rgba(255, 102, 255, 0.1)',
                  borderColor: 'rgba(255, 102, 255, 1)',
                  borderWidth: 1
                }
              ]
            },
            options: {
              scales: {
                y: {
                  type: 'logarithmic',
                  beginAtZero: true,
                }
              }
            }
          });
        </script>

        <h3 text-transform: lowercase; text-align: center;>每日所需微量元素(mg)</h3>
        <div class="chart-container">
          <canvas id="polarAreaChart"></canvas>
        </div>
        <script>
          const ctx1 = document.getElementById('polarAreaChart');

          new Chart(ctx1, {
            type: 'polarArea',
            data: {
              labels: ['Potassium (K)', 'Sodium (Na)', 'Calcium(Ca)', 'Phosphorus (P)', 'Magnesium (Me)', 'Iodine (I)', 'Iron (Fe)', 'Zinc(Zn)', 'Fluoride (F)'],
              datasets: [
                {
                  label: '男',
                  data: [2800, 2300, 1066, 866, 368, 150, 11.6, 15, 3],
                  backgroundColor: ['rgba(54, 162, 235, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'],
                  borderColor: ['rgba(54, 162, 235, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'],
                  borderWidth: 1
                },
                {
                  label: '女',
                  data: [2500, 2300, 1066, 866, 316, 150, 13.3, 12, 3],
                  backgroundColor: ['rgba(54, 162, 235, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'],
                  borderColor: ['rgba(54, 162, 235, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'],
                  borderWidth: 1
                }
              ]
            },
            options: {
              scales: {
                r: {
                  beginAtZero: true,
                  title: {
                    display: true,
                    text: 'Daily Recommended Intake (mg)'
                  }
                }
              },
              plugins: {
                legend: {
                  position: 'top',
                },
                tooltip: {
                  callbacks: {
                    label: function (tooltipItem) {
                      return tooltipItem.label + ': ' + tooltipItem.raw + ' mg';
                    }
                  }
                }
              }
            }
          });
        </script>



      </article>
      <article id="work">
        <h2 class="major">營養成分與食物建議</h2>
        <span class="image main"><img src="{{ url_for('static', filename='html_p/images/food1.png') }}" alt="" /></span>
        <form action="/submit" method="post">
          <div style="border: 2px gray solid; padding: 10px">
            <h2>請輸入基本資訊:</h2>
            <select name="gender">
              <option value="男性">男性</option>
              <option value="女性">女性</option>
            </select><br />
            <select name="age_group">
              <option value="13-15歲">13-15歲</option>
              <option value="16-18歲">16-18歲</option>
              <option value="19-30歲">19-30歲</option>
              <option value="31歲-50歲">31歲-50歲</option>
              <option value="51歲-70歲">51歲-70歲</option>
              <option value="71歲以上">71歲以上</option>
            </select><br />
            請輸入身高: <input type="text" name="height" /><br />
            請輸入體重: <input type="text" name="weight" /><br />
            <h2>請選擇現在的身心狀況:</h2>
            <div>
              心血管方面:<br />
              <input type="checkbox" name="conditions" value="糖尿病" class="btn-check" id="option1" />
              <label for="option1">糖尿病</label>
              <input type="checkbox" name="conditions" value="高血壓" class="btn-check" id="option2" />
              <label for="option2">高血壓</label>
              <input type="checkbox" name="conditions" value="肥胖" class="btn-check" id="option3" />
              <label for="option3">肥胖</label>
            </div>
            <br />
            <div>
              賀爾蒙方面:<br />
              <input type="checkbox" name="conditions" value="更年期" class="btn-check" id="option4" />
              <label for="option4">更年期</label>
            </div>
            <br />
            <div>
              免疫力方面:<br />
              <input type="checkbox" name="conditions" value="過敏性鼻炎" class="btn-check" id="option5" />
              <label for="option5">過敏性鼻炎</label>
            </div>
            <br />
            <div>
              神經精神系統:<br />
              <input type="checkbox" name="conditions" value="失眠" class="btn-check" id="option6" />
              <label for="option6">失眠</label>
              <input type="checkbox" name="conditions" value="憂鬱" class="btn-check" id="option7" />
              <label for="option7">憂鬱</label>
            </div>
            <br />
            <div>
              肌肉骨骼:<br />
              <input type="checkbox" name="conditions" value="骨質疏鬆" class="btn-check" id="option8" />
              <label for="option8">骨質疏鬆</label>
              <input type="checkbox" name="conditions" value="肌少症" class="btn-check" id="option9" />
              <label for="option9">肌少症</label>
              <input type="checkbox" name="conditions" value="運動後易痠痛" class="btn-check" id="option10" />
              <label for="option10">運動後易痠痛</label>
            </div>
            <br />
            <div>
              腸胃系統:<br />
              <input type="checkbox" name="conditions" value="便秘" class="btn-check" id="option11" />
              <label for="option11">便秘</label>
              <input type="checkbox" name="conditions" value="脹氣" class="btn-check" id="option12" />
              <label for="option12">脹氣</label>
              <input type="checkbox" name="conditions" value="胃食道逆流" class="btn-check" id="option13" />
              <label for="option13">胃食道逆流</label>
              <input type="checkbox" name="conditions" value="消化不良" class="btn-check" id="option14" />
              <label for="option14">消化不良</label>
            </div>
            <br />
            <div>
              生活習慣:<br />
              <input type="checkbox" name="conditions" value="生活壓力" class="btn-check" id="option15" />
              <label for="option15">生活壓力</label>
              <input type="checkbox" name="conditions" value="疲倦" class="btn-check" id="option16" />
              <label for="option16">疲倦</label>
              <input type="checkbox" name="conditions" value="體重控制" class="btn-check" id="option17" />
              <label for="option17">體重控制</label>
              <input type="checkbox" name="conditions" value="飲酒" class="btn-check" id="option18" />
              <label for="option18">飲酒</label>
              <input type="checkbox" name="conditions" value="青春痘" class="btn-check" id="option19" />
              <label for="option19">青春痘</label>
              <input type="checkbox" name="conditions" value="用眼過度" class="btn-check" id="option20" />
              <label for="option20">用眼過度</label>
            </div>
            <br /><br />
            <button type="submit" class="submitBtn">送出</button>
            <button type="reset">清除</button>
          </div>
        </form>
      </article>
      <article id="about">
        <h2 class="major">AI營養食物諮詢</h2>
        <span class="image main"><img src="{{ url_for('static', filename='html_p/images/ai.jpg') }}" alt="" /></span>
        <form method="post" action="#">
          <h2>我想詢問AI.....</h2>
          <textarea name="mytext" rows="6" cols="40" required></textarea>
          <button type="submit" class="submitBtn">送出</button>
          <button type="reset">清除</button>
        </form>
      </article>
      <article id="contact">
        <h2 class="major">Contact</h2>
        <form method="post" action="#">
          <div class="fields">
            <div class="field half">
              <label for="name">Name</label>
              <input type="text" name="name" id="name" />
            </div>
            <div class="field half">
              <label for="email">Email</label>
              <input type="text" name="email" id="email" />
            </div>
            <div class="field">
              <label for="message">Message</label>
              <textarea name="message" id="message" rows="4"></textarea>
            </div>
          </div>
          <ul class="actions">
            <li>
              <input type="submit" value="Send Message" class="primary" />
            </li>
            <li><input type="reset" value="Reset" /></li>
          </ul>
        </form>
        <ul class="icons">
          <li>
            <a href="#" class="icon brands fa-twitter"><span class="label">Twitter</span></a>
          </li>
          <li>
            <a href="#" class="icon brands fa-facebook-f"><span class="label">Facebook</span></a>
          </li>
          <li>
            <a href="#" class="icon brands fa-instagram"><span class="label">Instagram</span></a>
          </li>
          <li>
            <a href="#" class="icon brands fa-github"><span class="label">GitHub</span></a>
          </li>
        </ul>
      </article>
    </div>
    <footer id="footer">
      <p>
        &copy; Untitled. Design: <a href="https://html5up.net">HTML5 UP</a>.
      </p>
    </footer>
  </div>
  <div id="bg"></div>
  <script src="{{ url_for('static', filename='html_p/assets/js/jquery.min.js') }}"></script>
  <script src="{{ url_for('static', filename='html_p/assets/js/browser.min.js') }}"></script>
  <script src="{{ url_for('static', filename='html_p/assets/js/breakpoints.min.js') }}"></script>
  <script src="{{ url_for('static', filename='html_p/assets/js/util.js') }}"></script>
  <script src="{{ url_for('static', filename='html_p/assets/js/main.js') }}"></script>
</body>

# </html>
# """

# components.html(html_content, height=600)
