import {isObject} from "lodash";

function getHost() {
  let baseHost = ''
  try {
    baseHost = import.meta.env.VITE_API_HOST ?? document.location.host
  } catch (e) {
    console.error('Environment: get', e)
  }
  if (!baseHost) return ''
  const useSecureProtocol = baseHost.endsWith('.com')
  return `http${useSecureProtocol ? 's' : ''}://${baseHost}`
}

export const API_HOST = getHost()

export type TypedResponse<T> = Response & {
  data: T
}

export async function get<T>(url: string, params?: Record<string, string> | URLSearchParams): Promise<TypedResponse<T>> {
  url = `${API_HOST}${url}`
  if (isObject(params)) {
    url = `${url}?${new URLSearchParams(params).toString()}`
  }
  const response = (await fetch(url, {})) as TypedResponse<T>
  response.data = await response.json()
  return response
}

export default { get }
