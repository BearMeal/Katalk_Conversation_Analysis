const form = document.querySelector('form');

form.addEventListener('submit', async (event) => {
    event.preventDefault();

    // Show loading text and start updating it
    const loadingDiv = document.querySelector('#loading');
    toggleButton1.style.display = 'none'; // Initially hide the button
    toggleButton2.style.display = 'none'; // Initially hide the button
    toggleButton3.style.display = 'none'; // Initially hide the button

    loadingDiv.style.display = 'block';

    const loadingInterval = setInterval(updateLoadingText, 500);

    const formData = new FormData(form);
    var errorboom = false;

    let data;
    try {
        const responsePromise = fetch('/', {
            method: 'POST',
            body: formData,
        });

        // Wait for both the response and the minimum 3 seconds
        const [response] = await Promise.all([responsePromise, sleep(3000)]);

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        data = await response.json();
    } catch (error) {
        // Handle the error and display "오류 발생"
        console.error('Error:', error);
        data = { result: [['에러 발생']] };
        errorboom = true;
    } finally {
        // Stop updating and hide loading text
        clearInterval(loadingInterval);
        loadingDiv.style.display = 'none';
    }

    if (!errorboom) {
        toggleButton1.style.display = 'block';
        toggleButton2.style.display = 'block';
        toggleButton3.style.display = 'block'; // Show the Model 1 button

        const chartContainer1 = document.querySelector('#chartContainer1');
        chartContainer1.style.display = 'none';
        drawModel1Chart(data.result);
        const chartContainer2 = document.querySelector('#chartContainer2');
        chartContainer2.style.display = 'none';
        drawModel2Charts(data.result2)
        const chartContainer3 = document.querySelector('#chartContainer3');
        chartContainer3.style.display = 'none';
        drawModel3Charts(data.result3)

    } else {
        const resultDiv = document.querySelector('#result');
        resultDiv.innerHTML = data.result;
    }
});

const toggleButton1 = document.getElementById('toggleButton1');
const toggleButton2 = document.getElementById('toggleButton2');
const toggleButton3 = document.getElementById('toggleButton3');

toggleButton1.style.display = 'none'; // Initially hide the button
toggleButton2.style.display = 'none'; // Initially hide the button
toggleButton3.style.display = 'none'; // Initially hide the button


toggleButton1.addEventListener('click', () => {
    const chartContainer1 = document.querySelector('#chartContainer1');
    const chartContainer2 = document.querySelector('#chartContainer2');
    const chartContainer3 = document.querySelector('#chartContainer3');
    chartContainer2.style.display = 'none';
    chartContainer3.style.display = 'none';

    if (chartContainer1.style.display === 'none') {
        chartContainer1.style.display = 'block';
        drawModel1Chart(data.result);
    } else {
        chartContainer1.style.display = 'none';
    }
});

toggleButton2.addEventListener('click', () => {
    const chartContainer1 = document.querySelector('#chartContainer1');
    const chartContainer2 = document.querySelector('#chartContainer2');
    const chartContainer3 = document.querySelector('#chartContainer3');

    chartContainer1.style.display = 'none';
    chartContainer3.style.display = 'none';

    if (chartContainer2.style.display === 'none') {
        chartContainer2.style.display = 'block';
        drawModel2Charts(data.result2);
        //toggleButton1.classList.add('active'); // Add "active" class to the button
    } else {
        chartContainer2.style.display = 'none';
        //toggleButton1.classList.remove('active'); // Remove "active" class from the button
    }
});

toggleButton3.addEventListener('click', () => {
    const chartContainer1 = document.querySelector('#chartContainer1');
    const chartContainer2 = document.querySelector('#chartContainer2');
    const chartContainer3 = document.querySelector('#chartContainer3');

    chartContainer1.style.display = 'none';
    chartContainer2.style.display = 'none';

    if (chartContainer3.style.display === 'none') {
        chartContainer3.style.display = 'block';
        drawModel3Charts(data.result3);
        //toggleButton1.classList.add('active'); // Add "active" class to the button
    } else {
        chartContainer3.style.display = 'none';
        //toggleButton1.classList.remove('active'); // Remove "active" class from the button
    }
});

let myChart1;
let myPieChart1;// Declare myChart outside of drawBarChart function
let myPieChart2;
let myPieChart3;
let myPieChart4;

function drawModel1Chart(result) {
    const labels = [result[0][0], result[1][0]];
    const data = {
        labels: labels,
        datasets: [
            {
                label: '긍정문장 갯수',
                data: [result[0][1], result[1][1]],
                
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            },
            {
                label: '부정문장 갯수',
                data: [result[0][2], result[1][2]],
                
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                borderColor: 'rgba(255, 99, 132, 1)',
                borderWidth: 1
            }
        ]
    };

    // Destroy the previous chart
    if (myChart1) {
        myChart1.destroy();
    }

    const config = {
        type: 'bar',
        data: data,
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    stacked: true
                },
                x: {
                    stacked: true
                }
            }
        }
    };

    myChart1 = new Chart(
        document.getElementById('myChart1'),
        config
    );
}

// 모델2 파이그래프 1
function drawModel2Charts(result) {
    const chartNames = [result[0][0], result[1][0]];
    const labels = ['매우부정', '부정', '중립', '긍정', '매우긍정'];

    const createPieConfig = (chartName, data, colors) => {
  return {
    type: 'pie',
    data: {
      labels: labels,
      datasets: [{
        label: chartName,
        data: data,
        backgroundColor: colors,
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        tooltip: {
            callbacks: {
              label: function (context) {
                const label = context.label || '';
                const value = context.formattedValue || '';
                return `${label}: ${value}`;
              }
            }
          },
        legend: {
          display: false
        },
        title: {
          display: true,
          text: chartName,
          position: 'bottom'
        }
      },
    }
  };
};

    const colors = [  
    'rgba(76, 0, 76, 1)',
      'rgba(153, 0, 153, 1)',
        'rgba(153, 50, 204, 1)',
          'rgba(153, 102, 153, 1)',
            'rgba(229, 204, 229, 1)'];

    const pieChart1Config = createPieConfig(chartNames[0], result[0][1], colors);
    const pieChart2Config = createPieConfig(chartNames[1], result[1][1], colors);

    if (myPieChart1) {
        myPieChart1.destroy();
    }

    if (myPieChart2) {
        myPieChart2.destroy();
    }
    
    myPieChart1 = new Chart(
        document.getElementById('myPieChart2-1'),
        pieChart1Config
    );

    myPieChart2 = new Chart(
        document.getElementById('myPieChart2-2'),
        pieChart2Config
    );

    // 추가: 문장 데이터를 출력
    const createSentences = (containerId, negativeData, positiveData) => {
        const container = document.getElementById(containerId);
        const tbody = container.querySelector('tbody');
        tbody.innerHTML = '';
    
        const tr1 = document.createElement('tr');
        const th1 = document.createElement('th');
        th1.textContent = '매우부정';
        th1.style.color = 'red';
        tr1.appendChild(th1);
        tbody.appendChild(tr1);
    
        negativeData.forEach(sentence => {
            const tr = document.createElement('tr');
            const td = document.createElement('td');
            td.textContent = sentence;
            td.style.color = 'red';
            tr.appendChild(td);
            tbody.appendChild(tr);
        });
    
        const tr2 = document.createElement('tr');
        const th2 = document.createElement('th');
        th2.textContent = '매우긍정';
        th2.style.color = 'blue';
        tr2.appendChild(th2);
        tbody.appendChild(tr2);
    
        positiveData.forEach(sentence => {
            const tr = document.createElement('tr');
            const td = document.createElement('td');
            td.textContent = sentence;
            td.style.color = 'blue';
            tr.appendChild(td);
            tbody.appendChild(tr);
        });
    };

    createSentences('chart2-1Sentences', result[0][2], result[0][3]);
    createSentences('chart2-2Sentences', result[1][2], result[1][3]);
}

function drawModel3Charts(result) {
    const chartNames = [result[0][0], result[1][0]];
  
    const createPieConfig = (chartName, data, backgroundColor, labels) => {
        return {
          type: 'pie',
          data: {
            labels: labels,
            datasets: [{
              label: chartName,
              data: data,
              backgroundColor: backgroundColor,
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              tooltip: {
                  callbacks: {
                    label: function (context) {
                      const label = context.label || '';
                      const value = context.formattedValue || '';
                      return `${label}: ${value}`;
                    }
                  }
                },
              legend: {
                display: false
              },
              title: {
                display: true,
                text: chartName,
                position: 'bottom'
              }
            },
          }
        };
      };
  
      const labels1 = result[0][2];
      const labels2 = result[1][2];
      const labels = [...new Set([...labels1, ...labels2])]; // 중복된 항목을 제거한 후, 하나의 배열로 합침
      
      const colors = {
        '놀람': 'rgba(76, 0, 76, 1)',
        '슬픔': 'rgba(153, 0, 153, 1)',
        '행복': 'rgba(153, 50, 204, 1)',
        '중립': 'rgba(153, 102, 153, 1)',
        '분노': 'rgba(204, 0, 204, 1)',
        '공포': 'rgba(204, 51, 255, 1)',
        '혐오': 'rgba(229, 204, 229, 1)'
      };
      
      const backgroundColors = labels.map(label => colors[label]);
      
      const pieChart3Config = createPieConfig(chartNames[0], result[0][1], backgroundColors, labels);
      const pieChart4Config = createPieConfig(chartNames[1], result[1][1], backgroundColors, labels);
      
      if (myPieChart3) {
        myPieChart3.destroy();
      }
      
      if (myPieChart4) {
        myPieChart4.destroy();
      }
      
      myPieChart3 = new Chart(
        document.getElementById('myPieChart3-1'),
        pieChart3Config
      );
      
      myPieChart4 = new Chart(
        document.getElementById('myPieChart3-2'),
        pieChart4Config
      );
}

function updateLoadingText() {
    const loadingDiv = document.querySelector('#loading');
    const loadingText = loadingDiv.textContent;
    if (loadingText.length < 6) {
        loadingDiv.textContent += '.';
    } else {
        loadingDiv.textContent = '분석중';
    }
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

const inputFile = document.querySelector('input[type="file"]');
inputFile.addEventListener('change', () => {
    const resultDiv = document.querySelector('#result');
    resultDiv.innerHTML = '';        
    const chartContainer1 = document.getElementById('chartContainer1');
    chartContainer1.style.display='none';
    const chartContainer2 = document.getElementById('chartContainer2');
    chartContainer2.style.display='none';
    const chartContainer3 = document.getElementById('chartContainer3');
    chartContainer3.style.display='none';
    const toggleButton1 = document.getElementById('toggleButton1');
    const toggleButton2 = document.getElementById('toggleButton2');
    const toggleButton3 = document.getElementById('toggleButton3');

    toggleButton1.style.display = 'none'; // Initially hide the button
    toggleButton2.style.display = 'none'; // Initially hide the button
    toggleButton3.style.display = 'none'; // Initially hide the button

});