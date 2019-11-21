var App = new Vue({
    el: '#app',
    data: {
        target: 'html',
        file: false,
        dragging: false,
        header: null,
    },
    delimiters: ['${', '}'],
    methods: {
        change: function(e) {
            this.dragging = false
            var file = e.target.files
            var reader = new FileReader()
            reader.readAsText(file[0]);
            reader.onload = function (ev) {
            }
            data = {
                name: file[0].name,
                path: file[0].path,
            }
            console.log(file[0])
            this.file = data
            axios.post('/csvresponce', {
                path: this.file.path
            })
            .then(response => {
                this.header = response.data
            }).catch(error => {
                console.log(error);
            });
        },
        clear: function() {
            document.getElementById("file").value = ""
        },
        remove: function () {
            this.file = false
        }
    }
})