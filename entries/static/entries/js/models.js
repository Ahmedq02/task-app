class Task {
    constructor(id, email, description, dueBy, priority, isUrgent) {
        this.id = id;
        this.email = email;
        this.description = description;
        this.dueBy = dueBy;
        this.priority = priority;
        this.isUrgent = isUrgent;
    }

    static fromJson(json) {
        return new Task(
            json.id,
            json.email,
            json.description,
            json.due_by,
            json.priority,
            json.is_urgent,
        );
    }

    toJson() {
        return {
            id: this.id,
            email: this.email,
            description: this.description,
            due_by: this.dueBy,
            priority: this.priority,
            is_urgent: this.isUrgent,
        };
    }
}