export interface ListResponse<T extends any> {
    success: boolean;
    message: string;
    data: Array<T>;
    metadata?: Record<string, any>;
}