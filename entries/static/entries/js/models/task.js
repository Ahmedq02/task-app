class Task {
    constructor(id, email, task, dueBy, priority, isUrgent) {
        this.id = id;
        this.email = email;
        this.task = task;
        this.dueBy = dueBy;
        this.priority = priority;
        this.isUrgent = isUrgent;
    }

    static fromJson(json) {
        return new Task(
            json.id,
            json.email,
            json.task,
            json.due_by,
            json.priority,
            json.is_urgent,
        );
    }

    toJson() {
        return {
            id: this.id,
            email: this.email,
            task: this.task,
            due_by: this.dueBy,
            priority: this.priority,
            is_urgent: this.isUrgent,
        };
    }
}

export { Task };