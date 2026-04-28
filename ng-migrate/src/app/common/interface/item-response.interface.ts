export interface ItemResponse<T extends any> {
    success: boolean;
    message: string;
    data: T;
    metadata?: Record<string, any>;
}