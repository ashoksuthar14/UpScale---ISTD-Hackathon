function vote(type, id, value) {
    fetch(`/vote/${type}/${id}/${value}`)
        .then(response => response.json())
        .then(data => {
            document.querySelector(`#votes-${type}-${id}`).textContent = data.votes;
        });
} 