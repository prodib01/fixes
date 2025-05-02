export interface Iuser {
    id: number;
    email: string;
    is_active: boolean;
    email_verified: boolean;
    date_joined: string;
}
export interface IUserProfile {
    id: number;
    dob: string | null;
    emergency_contact: string | null;
    emergency_phone: string | null;
    first_name: string;
    last_name: string;
    other_name: string | null;
    gender: string | null;
    phone: string;
    profile_picture: string | null;
    user: Iuser;
    user_type: string;
}