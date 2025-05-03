export interface Iuser {
    id: number
    email: string
    is_active: boolean
    email_verified: boolean
    date_joined: string
  }
  export interface IUserProfile {
    id: number
    dob: string | null
    emergency_contact: string | null
    emergency_phone: string | null
    first_name: string
    last_name: string
    other_name: string | null
    gender: string | null
    phone: string
    profile_picture: string | null
    user: Iuser
    user_type: string
  }
  
  export interface ISchool {
    id: number
    name: string
    logo: string | null
    is_active: boolean
    created_at: string
    updated_at: string
    school_settings: Record<string, any>
    owner: number
  }
  
  export interface ICampus {
    id: number
    school_type: string
    category: string
    country: string
    name: string
    website: string
    address: string
    city: string
    state: string
    phone: string
    email: string
    is_active: boolean
    coordinates: any
    code: string
    created_at: string
    updated_at: string
    school: number
  }
  