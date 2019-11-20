var App = new Vue({
    el: '#app',
    data: {
        files: [],
        dragging: false,
    },
    delimiters: ['${', '}'],
    methods: {
        change: function(e) {
            var file = e.target.files
            var reader = new FileReader()
            reader.readAsText(file[0]);
            reader.onload = function (ev) {
            }
            pos = this.files.length
            data = {
                name: file[0].name,
                path: file[0].path,
            }
            console.log(file[0])
            this.$set(this.files, pos, data)
        },
        clear: function() {
            document.getElementById("file").value = ""
        },
        remove: function(n) {
            this.files.splice(n, 1);
        }
    }
})