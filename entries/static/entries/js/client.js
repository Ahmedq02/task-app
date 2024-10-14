import { TaskService } from './services/task.js';

class Configuration {
    // TODO: Change this URL to relative URL
    constructor(basePath = undefined, headers = {}) {
        if(basePath === undefined) {
            basePath = window.location.origin;
        }
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