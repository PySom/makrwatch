const handleInvalidModel = (model) => {
    let build;
    if (model) {
        if (Array.isArray(model)) {
            build = model.reduce((aggregate, { _, errorMessage }) => {
                console.log(errorMessage)
                aggregate = aggregate.concat(errorMessage)
                return aggregate;
            }, []).join(' ')
        }
        else {
            build = Object.entries(model).reduce((aggregate, [key, value]) => {
                aggregate = aggregate.concat(value)
                return aggregate;
            }, []).join(' ')
        }
    }
    console.log(build, model)
    build = build && build.toString()
    return build;
}

export const handleError = (err, name) => {
    console.log(err.response)
    const { status, data } = typeof (err) === "object" ? err.response : {};
    if (!status) {
        console.log(err);
        return "An unknown error occured at this time. Please try again";
    }
    if (status === 404) {
        return `${name || 'item'} not found in our logs.`;
    }
    else if (status === 500) {
        return "This is an issue from us. Please feel free to report this issue.";
    }
    else {
        const { errors, title } = data;
        if (title) {
            return title.toString();
        }
        if (errors) {
            return handleInvalidModel(errors)
        }
    }
}