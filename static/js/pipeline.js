document.addEventListener('DOMContentLoaded', function() {
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    const csrftoken = getCookie('csrftoken');
    
    // Initialize SortableJS on all kanban columns
    const stageContainers = document.querySelectorAll('.kanban-stage-list');
    
    stageContainers.forEach(container => {
        new Sortable(container, {
            group: 'pipeline',
            animation: 150,
            ghostClass: 'sortable-ghost',
            dragClass: 'sortable-drag',
            onEnd: function (evt) {
                const itemEl = evt.item;
                const toContainer = evt.to;
                
                const dealId = itemEl.getAttribute('data-deal-id');
                const newStageId = toContainer.id.replace('stage-', '');
                
                // Only send request if stage changed
                if (evt.from !== toContainer) {
                    // Make API call to update stage
                    fetch('/pipeline/deal/update-stage/', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'X-CSRFToken': csrftoken
                        },
                        body: JSON.stringify({
                            'deal_id': dealId,
                            'new_stage_id': newStageId
                        })
                    })
                    .then(response => response.json())
                    .then(data => {
                        if (data.success) {
                            window.location.reload();
                        } else {
                            console.error('Error updating stage:', data.error);
                            alert('Erro ao atualizar estágio. A página será recarregada.');
                            window.location.reload();
                        }
                    })
                    .catch(error => {
                        console.error('Error:', error);
                        alert('Erro ao atualizar estágio. A página será recarregada.');
                        window.location.reload();
                    });
                }
            },
        });
    });
    
    // Setup ghost class styles if not in css
    const style = document.createElement('style');
    style.innerHTML = `
        .sortable-ghost {
            opacity: 0.4;
            background-color: #1e293b;
        }
        .sortable-drag {
            cursor: grabbing !important;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.5);
        }
    `;
    document.head.appendChild(style);
});
