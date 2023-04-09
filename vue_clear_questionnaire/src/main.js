import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import axios from 'axios'
import VueAxios from 'vue-axios'
import VueClipboard from 'vue-clipboard2'

Vue.use(VueAxios, axios)
Vue.use(VueClipboard)
Vue.config.productionTip = false

import {
    Button, Field, Form,
    Tabbar, TabbarItem, Swipe,
    SwipeItem, Lazyload, List, PullRefresh,
    Cell, CellGroup, Tab, Tabs, NavBar, Divider,
    CountDown, Dialog, Uploader, Icon, Sticky,
    Empty, Search, ShareSheet, ActionSheet,
    RadioGroup, Radio, Checkbox, CheckboxGroup,
    Switch, Stepper, Picker, Popup, Popover,
    Image as VanImage, Toast, Grid, GridItem,
    Pagination, Collapse, CollapseItem, Card,
    Loading, Skeleton, Col, Row, DropdownMenu, DropdownItem

} from 'vant';

Vue.config.productionTip = false
Vue.use(Button)
Vue.use(Field)
Vue.use(Form)
Vue.use(Tabbar)
Vue.use(TabbarItem)
Vue.use(Swipe)
Vue.use(SwipeItem)
Vue.use(Lazyload, {
    lazyComponent: true,
})
Vue.use(List)
Vue.use(PullRefresh)
Vue.use(Cell)
Vue.use(CellGroup)
Vue.use(Tab)
Vue.use(Tabs)
Vue.use(NavBar)
Vue.use(Divider)
Vue.use(CountDown)
Vue.use(VanImage)
Vue.use(Dialog)
Vue.use(Uploader)
Vue.use(Icon)
Vue.use(Sticky)
Vue.use(Empty)
Vue.use(Search)
Vue.use(ShareSheet)
Vue.use(ActionSheet)
Vue.use(RadioGroup)
Vue.use(Radio)
Vue.use(Checkbox)
Vue.use(CheckboxGroup)
Vue.use(Switch)
Vue.use(Stepper)
Vue.use(Picker)
Vue.use(Popup)
Vue.use(Popover)
Vue.use(Toast)
Vue.use(Grid)
Vue.use(GridItem)
Vue.use(Pagination)
Vue.use(Collapse)
Vue.use(CollapseItem)
Vue.use(Card)
Vue.use(Loading)
Vue.use(Skeleton)
Vue.use(Col)
Vue.use(Row)
Vue.use(DropdownMenu)
Vue.use(DropdownItem)

import {
    Button as elButton, Select as elSelect, Avatar as elAvatar,
    Card as elCard, Link as elLink, Table as elTable, TableColumn as elTableColumn,
    Progress as elProgress, Pagination as elPagination, Image as elImage, Carousel as elCarousel,
    CarouselItem as elCarouselItem
} from 'element-ui';

Vue.use(elButton)
Vue.use(elSelect)
Vue.use(elAvatar)
Vue.use(elCard)
Vue.use(elLink)
Vue.use(elTable)
Vue.use(elTableColumn)
Vue.use(elProgress)
Vue.use(elPagination)
Vue.use(elImage)
Vue.use(elCarousel)
Vue.use(elCarouselItem)

Toast.setDefaultOptions({duration: 3000})
new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app')
