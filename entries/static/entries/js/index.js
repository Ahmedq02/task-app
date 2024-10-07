import { APIClient, Configuration } from "./client";

const client = new APIClient(new Configuration(headers = {
    'X-CSRFToken': '{{ csrf_token }}',
}));