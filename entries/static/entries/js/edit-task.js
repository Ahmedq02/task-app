import { APIClient, Configuration } from './client.js';
import { Task, CreateTask, Priority } from './models/task.js';

class TaskForm {
    constructor(taskId=null) {
        this.taskId = taskId;

        this.form = document.querySelector('.task-form');

        this.emailField = document.getElementById('id_user_email');
        this.taskField = document.getElementById('id_task');
        this.dueByField = document.getElementById('id_due_by');
        this.priorityField = document.getElementById('id_priority');
        this.isUrgentField = document.getElementById('id_is_urgent');

        this.csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
        this.client = new APIClient(new Configuration(undefined, {
            'X-CSRFToken': this.csrfToken,
        }));

        this.form.addEventListener('submit', this.submit.bind(this));
    
        console.log(this.taskId);
        if(this.taskId !== undefined && this.taskId !== null) {
            this.loadTask(taskId);
        }
    }

    async loadTask(taskId) {
        const task = await this.client.tasks.getTask(taskId);
        console.log(task);

        this.emailField.value = task.email;
        this.taskField.value = task.task;
        this.dueByField.value = task.dueBy.toISOString().slice(0, 16);
        this.priorityField.value = task.priority.toInt();
        this.isUrgentField.checked = task.isUrgent;
    }

    getFormData() {
        return {
            email: this.emailField.value,
            task: this.taskField.value,
            dueBy: new Date(
                Date.parse(this.dueByField.value)),
            priority: Priority.fromInt(
                parseInt(this.priorityField.value)),
            isUrgent: this.isUrgentField.checked,
        };
    }

    async submit(event) {
        event.preventDefault();

        const data = this.getFormData();
        
        if(this.taskId) {
            const task = new Task(
                this.taskId,
                data.email,
                data.task,
                data.dueBy,
                data.priority,
                data.isUrgent
            )

            await this.client.tasks.updateTask(task);
        } else {
            const task = new CreateTask(
                data.email,
                data.task,
                data.dueBy,
                data.priority,
                data.isUrgent
            );
    
            await this.client.tasks.createTask(task);
        }
        
        
        const nextEvent = new CustomEvent('task-submitted');
        document.dispatchEvent(nextEvent);
    }
}

const onload = () => {
    let taskId = parseInt(document.getElementById("task-id").textContent);
    if(Number.isNaN(taskId)) {
        taskId = undefined;
    }

    const _ = new TaskForm(taskId);

    const entriesURL = document.getElementById('entries-url').textContent;
    document.addEventListener('task-submitted', () => {
        window.location.href = entriesURL;
    });
}

window.onload = onload;