class Priority {
    static LOW = new Priority(0, 'Low');
    static MEDIUM = new Priority(1, 'Medium');
    static HIGH = new Priority(2, 'High');

    constructor(intValue, stringValue) {
        this.intValue = intValue;
        this.stringValue = stringValue;
    }

    static fromInt(intValue) {
        switch (intValue) {
            case 0:
                return Priority.LOW;
            case 1:
                return Priority.MEDIUM;
            case 2:
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
        return {
            id: this.id,
            user_email: this.email,
            task: this.task,
            due_by: this.dueBy.toUTCString(),
            priority: this.priority.toJson(),
            is_urgent: this.isUrgent,
        };
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
        return {
            user_email: this.email,
            task: this.task,
            due_by: this.dueBy.toUTCString(),
            priority: this.priority.toJson(),
            is_urgent: this.isUrgent,
        };
    }
}

export { Task, CreateTask };