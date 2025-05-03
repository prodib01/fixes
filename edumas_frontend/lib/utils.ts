import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";
import { IUserProfile } from "./types";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

export function getUserProfile(): IUserProfile | null {
  if (typeof window === "undefined") return null;
  const userProfile = localStorage.getItem("userProfile");
  return userProfile ? JSON.parse(userProfile) : null;
}
