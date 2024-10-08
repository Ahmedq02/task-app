import { APIClient, Configuration } from "./client.js";

class TaskCard {
    constructor(task) {
        this.task = task;
    }

    render() {
        const card = document.createElement('li');
        card.className = 'card';

        card.innerHTML = `
            <h5 class="card-title">${this.task.task}</h5>
            <p class="card-text">Due by: ${this.task.dueBy.toLocaleString()}</p>
            <p class="card-text">Email: ${this.task.email}</p>
            <p class="card-text">Priority: ${this.task.priority.toString()}</p>
            <p class="card-text">Urgent: ${this.task.isUrgent}</p>
            <a href="{% url 'edit_task' task.id %}" class="button">Edit</a>
            <button class="button button-danger">Delete</button>
        `;

        const deleteButton = card.querySelector('.button-danger');
        deleteButton.addEventListener('click', async () => {
            const deleteEvent = new CustomEvent('taskDeleted', {
                detail: {
                    taskId: this.task.id,
                }
            });
            document.dispatchEvent(deleteEvent);
        });
        return card;
    }
}

const loadTasks = async (client) => {
    const parent = document.getElementById('task-cards');
    const tasks = await client.tasks.getTasks();
    parent.innerHTML = '';
    tasks.forEach(task => {
        const card = new TaskCard(task);;
        parent.appendChild(card.render());
    });
};

const deleteTask = async (id, client) => {
    console.log(id);
    console.log(await client.tasks.getTask(id));

    await client.tasks.deleteTask(id);
    loadTasks();
};


const onload = async () => {
    const client = new APIClient(new Configuration(undefined, {
        'X-CSRFToken': '{{ csrf_token }}',
    }));

    loadTasks(client);

    document.addEventListener('taskDeleted', async (event) => {
        await deleteTask(event.detail.taskId, client);
    });

};

window.onload = onload;