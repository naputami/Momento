import { createVuetify} from 'vuetify'
import * as components from "vuetify/components"
import * as directives from "vuetify/directives"
import { aliases, mdi } from 'vuetify/iconsets/mdi-svg'
import { mdiAccount, mdiLock, mdiChessQueen, mdiHome, mdiLogout, 
mdiShieldCrown, mdiHeart, mdiHeartOutline, mdiDelete, mdiCamera, mdiTextBox, mdiPencil } from '@mdi/js'
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
  defaults: {
    VTextField : {
      color: 'primary',
      variant: 'outlined'
    }
  },
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
      home: mdiHome,
      crown: mdiChessQueen,
      logout: mdiLogout,
      admin: mdiShieldCrown,
      heart: mdiHeart,
      heartOutline: mdiHeartOutline,
      delete: mdiDelete,
      camera: mdiCamera,
      pencil: mdiPencil,
      text: mdiTextBox
    },
    sets: {
      mdi,
    },
  },
  directives,
  components
})

export default vuetify