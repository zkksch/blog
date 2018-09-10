import Cookies from 'universal-cookie';


interface Options {
    [index: string]: any
}


function includeCredentials (options: Options) {
    // fetch doesn't includes credentials by default
    options.credentials = 'include';
    return options
}

function csrfProtected (options: Options) {
    // gets django csrf token from cookies and adds it in headers
    options.headers = {
        ...options.headers,
        "X-CSRFToken": (new Cookies()).get('csrftoken')
    };
    return options
}

export function safeFetch (url: string, options: Options) {
    // fetch for safe methods
    options = includeCredentials(options);
    return fetch(url, options)
}

export function unsafeFetch (url: string, options: Options) {
    // fetch for unsafe methods
    options = includeCredentials(options);
    options = csrfProtected(options);
    return fetch(url, options)
}
