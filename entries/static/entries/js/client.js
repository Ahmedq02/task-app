import { TaskService } from './services/task.js';

class Configuration {
    constructor(basePath = 'http://localhost:8000/api/v0/', headers = {}) {
        this.basePath = basePath;
        this.headers = headers;
    }
}

class APIClient {
    constructor(configuration = new Configuration()) {
        this.configuration = configuration;

        this.tasks = new TaskService(this);
    }

    do(method, path, queryParams={}, body = null, headers = {}) {
        const url = new URL(path, this.configuration.basePath);
        Object.keys(queryParams).forEach(key => url.searchParams.append(key, queryParams[key]));

        const request = new Request(url, {
            method: method,
            headers: new Headers({
                ...this.configuration.headers,
                ...headers,
            }),
            body: body,
        });

        return fetch(request);
    }
    
}

export { APIClient, Configuration };