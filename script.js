let time = 0;
let earnings = 0;
let timerInterval;

function startMining() {
    timerInterval = setInterval(() => {
        time++;
        earnings += Math.floor(Math.random() * 5) + 1; // Случайная прибыль
        document.getElementById("timer").innerText = `⏳ Время: ${time} сек`;
        document.getElementById("earned").innerText = `💰 Намайнено: ${earnings} RUB`;
    }, 1000);
}

document.getElementById("stopMining").addEventListener("click", () => {
    clearInterval(timerInterval);

    // Отправка данных в Telegram WebApp
    if (window.Telegram.WebApp) {
        Telegram.WebApp.sendData(JSON.stringify({ earned: earnings }));
        Telegram.WebApp.close();  // Закрываем WebApp
    }
});

// Автостарт анимации при загрузке
startMining();
