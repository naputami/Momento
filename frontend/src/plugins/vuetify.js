import { createVuetify} from 'vuetify'
import * as components from "vuetify/components"
import * as directives from "vuetify/directives"
import { aliases, mdi } from 'vuetify/iconsets/mdi-svg'
import { mdiAccount, mdiLock, mdiEye, mdiEyeOff, mdiChevronDoubleRight } from '@mdi/js'
import '@/sass/variable.scss'

const myTheme = {
    dark: false,
    colors: {
      background: '#e2f9fe',
      surface: '#FFFFFF',
      primary: '#006d77ff',
      'primary-variant': '#83c5beff',
      secondary: '#e29578ff',
      'secondary-variant': '#ffddd2ff',
      error: '#cd858c',
      info: '#2196F3',
      success: '#85cda2',
      warning: '#c685cd',
    },
  }

const vuetify = createVuetify({
  theme: {
    defaultTheme: 'myTheme',
    themes: {
        myTheme,
    }
  },
  icons: {
    defaultSet: 'mdi',
    aliases: {
      ...aliases,
      account: mdiAccount,
      password: mdiLock,
      hidePassword: mdiEye,
      showPassword: mdiEyeOff,
      chevronRight: mdiChevronDoubleRight
    },
    sets: {
      mdi,
    },
  },
  directives,
  components
})

export default vuetify