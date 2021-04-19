var cached_graph_def = {}
var tooltip_timeout = null

Vue.component('chartjs', {
    template:
    `<canvas  v-bind:id="jp_props.id" :class="jp_props.classes"  :style="jp_props.style" :width="jp_props.width" height="jp_props.height"></canvas>`,
    methods: {
        graphjs_change() {
            cached_graph_def[this.$props.jp_props.id] = JSON.stringify(this.$props.jp_props.def);
            var id = this.$props.jp_props.id.toString();
            var canvas = document.getElementById(id);
            ctx = canvas.getContext('2d');
            var c = new Chart(ctx).Line(this.$props.jp_props.def);
            //var c = new Chart(buyers).Line(this.$props.jp_props.def);
            //var btn = document.createElement("BUTTON");
            //btn.innerHTML = JSON.stringify(this.$props.jp_props.def);
            //document.body.appendChild(btn);
            cached_graph_def['chart'+id] = c;
        }
    },
    mounted() {
        this.graphjs_change();
    },
    updated() {

        const container = this.$props.jp_props.id.toString();
        const chart = cached_graph_def['chart' + container];
        if (!this.$props.jp_props.use_cache || (JSON.stringify(this.$props.jp_props.def) != cached_graph_def[this.$props.jp_props.id])) {
            cached_graph_def[this.$props.jp_props.id] = JSON.stringify(this.$props.jp_props.def);
            if (this.$props.jp_props.update_create) {
                this.graphjs_change();
            } else {
                chart.update(this.$props.jp_props.def, true, true, this.$props.jp_props.update_animation); //Look into chart.update
            }
        }

    },
    props: {
        jp_props: Object
    }
});
