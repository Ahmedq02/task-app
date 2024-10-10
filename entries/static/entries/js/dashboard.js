import { APIClient, Configuration } from './client.js';
import { Priority } from './models/task.js'

class PieChar {
    constructor(tasks) {
        this.tasks = tasks;

        this.labels = [
            Priority.LOW.toString(),
            Priority.MEDIUM.toString(),
            Priority.HIGH.toString()
        ]

        this.data = [
            this.tasks.filter(task => task.priority === Priority.LOW).length,
            this.tasks.filter(task => task.priority === Priority.MEDIUM).length,
            this.tasks.filter(task => task.priority === Priority.HIGH).length
        ]
    }

    render() {
        const ctx = document.getElementById("pie_chart").getContext("2d");
        this.chart = new Chart(ctx, {
            type: "pie",
            data: {
                labels: this.labels,
                datasets: [{
                    label: "Number of Tasks",
                    data: this.data,
                    backgroundColor: [
                        "rgb(35, 136, 35)",
                        "rgb(255, 191, 0)",
                        "rgb(210, 34, 45)"
                    ]
                }]
            }
        });
    }
}

class LineChart {
    constructor(tasks, startDate, endDate) {
        this.tasks = tasks;
        
        this.labels = [];
        this.data = [];

        for (let date = new Date(startDate); date <= endDate; date.setDate(date.getDate() + 1)) {
            this.labels.push(date.toDateString());
            this.data.push(this.tasks.filter(task => task.dueBy.toDateString() === date.toDateString()).length);
        }   
    }

    render() {
        const ctx = document.getElementById("line_chart").getContext("2d");
        this.chart = new Chart(ctx, {
            type: "line",
            data: {
                labels: this.labels,
                datasets: [{
                    label: "Number of Tasks Due",
                    data: this.data,
                    backgroundColor: "rgba(75, 192, 192, 0.2)",
                    borderColor: "rgba(75, 192, 192, 1)",
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    }
}

class TaskTable {
    constructor(tasks) {
        this.tasks = tasks;
    }

    render() {
        const parent = document.getElementById('task-table');
        this.tasks.forEach((task) => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${task.title}</td>
                <td>${task.dueBy.toLocaleString()}</td>
                <td>${task.email}</td>
                <td>${task.priority.toString()}</td>
                <td>${task.isUrgent}</td>
            `;
            parent.appendChild(row);
        });
    }
}

class UrgentTaskCounter {
    constructor(tasks) {
        this.tasks = tasks;
    }

    count() {
        return this.tasks.filter(task => task.isUrgent).length;
    }

    render() {
        const parent = document.getElementById('urgent-count');
        parent.innerHTML = `Urgent Tasks Count: ${this.count()}`;
    }
}

const onload = () => {
    const client = new APIClient(new Configuration());

    const today = new Date();
    const start_date = today;

    const end_date = new Date(today);
    end_date.setDate(today.getDate() + 30);

    const tasks = client.tasks.getTasks(start_date, end_date);
    tasks.then((tasks) => {
        const pieChart = new PieChar(tasks);
        pieChart.render();

        const lineChart = new LineChart(tasks, start_date, end_date);
        lineChart.render();

        const taskTable = new TaskTable(tasks);
        taskTable.render();

        const urgentTaskCounter = new UrgentTaskCounter(tasks);
        urgentTaskCounter.render();
    });
};

document.addEventListener('DOMContentLoaded', onload);