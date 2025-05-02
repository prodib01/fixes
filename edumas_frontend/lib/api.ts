import { IUserProfile } from "./types";

const API_BASE_URL =
  process.env.NEXT_PUBLIC_API_BASE_URL || "http://localhost:8000";

// Helper function to get the authentication token
export const getToken = (): string | null => {
  if (typeof window !== "undefined") {
    return localStorage.getItem("token");
  }
  return null;
};

// Helper function to set the authentication token
export const setLocalStorageConfigs = (token: string, userProfile: IUserProfile): void => {
  if (typeof window !== "undefined") {
    localStorage.setItem("token", token);
    localStorage.setItem("userProfile", JSON.stringify(userProfile));
  }
};

// Helper function to remove the authentication token (logout)
export const removeToken = (): void => {
  if (typeof window !== "undefined") {
    localStorage.removeItem("token");
  }
};

// Helper function to check if the user is authenticated
export const isAuthenticated = (): boolean => {
  return !!getToken();
};

// Helper function to create headers with authentication
const createHeaders = (includeAuth = true): HeadersInit => {
  const headers: HeadersInit = {
    "Content-Type": "application/json",
  };

  if (includeAuth) {
    const token = getToken();
    if (token) {
      headers["Authorization"] = `Bearer ${token}`;
    }
  }

  return headers;
};

// Generic API request function
const apiRequest = async <T>(
  endpoint: string,
  method: string = "GET",
  data?: any,
  requireAuth: boolean = true
): Promise<T> => {
  const url = `${API_BASE_URL}${endpoint}`;
  const options: RequestInit = {
    method,
    headers: createHeaders(requireAuth),
  };

  if (data) {
    options.body = JSON.stringify(data);
  }

  const response = await fetch(url, options);

  // Handle 401 Unauthorized responses
  if (response.status === 401 && requireAuth) {
    removeToken();
    // Redirect to login page if we're in a browser environment
    if (typeof window !== "undefined") {
      window.location.href = "/auth/login";
    }
    throw new Error("Authentication required");
  }

  const result = await response.json();

  if (!response.ok) {
    throw new Error(result.detail || result.error || "An error occurred");
  }

  return result as T;
};

// Authentication API functions with improved error handling
export const authAPI = {
  login: async (email: string, password: string) => {
    return apiRequest<{ token: string }>(
      "/accounts/login/",
      "POST",
      { email, password },
      false
    );
  },

  register: async (userData: {
    email: string;
    password: string;
    // user_type: string
    first_name: string;
    last_name: string;
    other_name?: string;
    gender?: string;
    dob?: string;
    phone?: string;
  }) => {
    return apiRequest("/accounts/register/", "POST", userData, false);
  },

  verifyEmail: async (email: string, otp: string) => {
    // Input validation
    if (!email) {
      throw new Error("Email address is required");
    }

    if (!otp) {
      throw new Error("Verification code is required");
    }

    try {
      // Make the API request to verify email with OTP
      const response = await apiRequest(
        "/accounts/verify-email/",
        "POST",
        { email, otp },
        false
      );

      console.log("Email verification successful:", response);
      return response;
    } catch (error: any) {
      console.error("Email verification failed:", error);

      // Handle specific errors
      let errorMessage = "An error occurred during verification";

      if (error.message.includes("Invalid OTP")) {
        errorMessage = "Invalid verification code. Please try again.";
      } else if (error.message.includes("expired")) {
        errorMessage =
          "Verification code has expired. Please request a new one.";
      } else if (error.message.includes("not found")) {
        errorMessage =
          "Email address not found or verification code is invalid.";
      }

      throw new Error(errorMessage);
    }
  },

  // The resendVerification function looks good as is, but let's enhance it slightly:
  resendVerification: async (email: string) => {
    if (!email) {
      throw new Error("Email address is required");
    }

    try {
      const response = await apiRequest(
        "/accounts/resend-verification/",
        "POST",
        { email },
        false
      );

      return response;
    } catch (error: any) {
      // Improved error handling
      let errorMessage = "Failed to resend verification code";

      if (error.message.includes("already verified")) {
        errorMessage = "This email is already verified. Please login.";
      } else if (error.message.includes("not found")) {
        errorMessage = "Email address not found in our system.";
      }

      throw new Error(errorMessage);
    }
  },
};

// User API functions
export const userAPI = {
  getProfile: async () => {
    return apiRequest("/accounts/profile/", "GET");
  },

  updateProfile: async (profileData: any) => {
    return apiRequest("/accounts/profile/", "PUT", profileData);
  },
};

// Student API functions
export const studentAPI = {
  getAll: async () => {
    return apiRequest("/students/", "GET");
  },

  getById: async (id: string) => {
    return apiRequest(`/students/${id}/`, "GET");
  },
};

// Course API functions
export const courseAPI = {
  getAll: async () => {
    return apiRequest("/courses/", "GET");
  },

  getById: async (id: string) => {
    return apiRequest(`/courses/${id}/`, "GET");
  },

  create: async (courseData: any) => {
    return apiRequest("/courses/", "POST", courseData);
  },

  update: async (id: string, courseData: any) => {
    return apiRequest(`/courses/${id}/`, "PUT", courseData);
  },

  delete: async (id: string) => {
    return apiRequest(`/courses/${id}/`, "DELETE");
  },
};

// School API functions
export const schoolAPI = {
  create: async (schoolData: any) => {
    return apiRequest("/schools/", "POST", schoolData);
  },

  getById: async (id: string) => {
    return apiRequest(`/schools/${id}/`, "GET");
  },

  update: async (id: string, schoolData: any) => {
    return apiRequest(`/schools/${id}/`, "PUT", schoolData);
  },

  delete: async (id: string) => {
    return apiRequest(`/schools/${id}/`, "DELETE");
  },
};
