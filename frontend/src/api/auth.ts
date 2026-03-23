import apiClient from "./client";

export interface LoginPayload {
  username: string; // The backend uses OAuth2PasswordRequestForm which expects 'username'
  password: string;
}

export interface RegisterPayload {
  email: string;
  password: string;
}

export interface TokenResponse {
  access_token: string;
  token_type: string;
}

export const authApi = {
  register: async (payload: RegisterPayload): Promise<TokenResponse> => {
    const { data } = await apiClient.post<TokenResponse>("/auth/register", payload);
    return data;
  },

  login: async (payload: LoginPayload): Promise<TokenResponse> => {
    // Backend expects form-urlencoded data for OAuth2PasswordRequestForm
    const formData = new URLSearchParams();
    formData.append("username", payload.username);
    formData.append("password", payload.password);
    const { data } = await apiClient.post<TokenResponse>("/auth/login", formData, {
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
    });
    return data;
  },

  getMe: async () => {
    const { data } = await apiClient.get("/auth/me");
    return data;
  },
};
