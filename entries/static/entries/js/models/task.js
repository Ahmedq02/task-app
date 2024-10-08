class Priority {
    static LOW = new Priority(1, 'Low');
    static MEDIUM = new Priority(2, 'Medium');
    static HIGH = new Priority(3, 'High');

    constructor(intValue, stringValue) {
        this.intValue = intValue;
        this.stringValue = stringValue;
    }

    static fromInt(intValue) {
        switch (intValue) {
            case 1:
                return Priority.LOW;
            case 2:
                return Priority.MEDIUM;
            case 3:
                return Priority.HIGH;
            default:
                throw new Error('Invalid priority value');
        }
    }

    static fromJson(json) {
        return Priority.fromInt(json);
    }

    toString() {
        return this.stringValue;
    }

    toInt() {
        return this.intValue;
    }

    toJson() {
        return this.toInt();
    }
}


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
            json.user_email,
            json.task,
            new Date(Date.parse(json.due_by)),
            Priority.fromJson(json.priority),
            json.is_urgent,
        );
    }

    toJson() {
        return JSON.stringify({
            id: this.id,
            user_email: this.email,
            task: this.task,
            due_by: this.dueBy.toISOString(),
            priority: this.priority.toJson(),
            is_urgent: this.isUrgent,
        });
    }
}


class CreateTask {
    constructor(email, task, dueBy, priority, isUrgent) {
        this.email = email;
        this.task = task;
        this.dueBy = dueBy;
        this.priority = priority;
        this.isUrgent = isUrgent;
    }

    toJson() {
        return JSON.stringify({
            user_email: this.email,
            task: this.task,
            due_by: this.dueBy.toISOString(),
            priority: this.priority.toJson(),
            is_urgent: this.isUrgent,
        });
    }
}

export { Task, CreateTask, Priority };