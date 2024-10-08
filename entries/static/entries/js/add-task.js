import { APIClient, Configuration } from './client.js';
import { CreateTask, Priority } from './models/task.js';

class TaskForm {
    constructor() {
        this.form = document.querySelector('.task-form');
        
        this.emailField = document.getElementById('id_user_email');
        this.taskField = document.getElementById('id_task');
        this.dueByField = document.getElementById('id_due_by');
        this.priorityField = document.getElementById('id_priority');
        this.isUrgentField = document.getElementById('id_is_urgent');

        this.csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

        this.form.addEventListener('submit', this.submit.bind(this));
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
        const task = new CreateTask(
            data.email,
            data.task,
            data.dueBy,
            data.priority,
            data.isUrgent
        );

        const client = new APIClient(new Configuration(undefined, {
            'X-CSRFToken': this.csrfToken,
        }));

        await client.tasks.createTask(task);
        this.form.reset();
    }
}

const onload = () => {
    const _ = new TaskForm();
}

window.onload = onload;