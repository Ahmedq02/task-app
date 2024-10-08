import { Task } from '../models/task.js';

class TaskService {

    constructor(client) {
        this.client = client;
    }

    async getTasks(startDate, endDate, status) {
        const queryParams = {
            start_date: startDate,
            end_date: endDate,
            status: status,
        };

        const response = await this.client.do(
            'GET', 
            './tasks', 
            queryParams,
        );

        if (!response.ok) {
            throw new Error('Failed to fetch tasks');
        }

        const json = await response.json();
        const items = json.items;
        
        return items.map(item => Task.fromJson(item));
    }

    async getTask(taskId) {
        const response = await this.client.do(
            'GET', 
            `./tasks/${taskId}`,
        );

        if (!response.ok) {
            console.error(response);
            throw new Error('Failed to fetch task');
        }

        const json = await response.json();
        return Task.fromJson(json);
    }

    async createTask(task) {
        const response = await this.client.do(
            'POST', 
            './tasks',
            body = task.toJson(),
            headers = {
                'Content-Type': 'application/json',
            },
        );

        if (!response.ok) {
            throw new Error('Failed to create task');
        }

        const json = await response.json();
        return Task.fromJson(json);
    }

    async deleteTask(taskId) {
        const response = await this.client.do(
            'DELETE', 
            `./tasks/${taskId}`,
        );

        if (!response.ok) {
            console.error(response);
            throw new Error('Failed to delete task');
        }
    }

    async updateTask(task) {
        const response = await this.client.do(
            'PUT', 
            `./tasks/${task.id}`,
            body = task.toJson(),
            headers = {
                'Content-Type': 'application/json',
            },
        );

        if (!response.ok) {
            throw new Error('Failed to update task');
        }

        const json = await response.json();
        return Task.fromJson(json);
    }
}

export { TaskService };