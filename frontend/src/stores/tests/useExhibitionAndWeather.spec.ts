import { setActivePinia, createPinia } from 'pinia'
import { useExhibitionAndWeather } from '../useExhibitionAndWeather'
import { getExhibitionAndWeather } from '@/apis/exhibitionAndWeather'
import { flushPromises } from '@vue/test-utils'
import { describe, it, expect, beforeEach, vi } from 'vitest'

vi.mock('@/apis/exhibitionAndWeather')
vi.mock('lodash', () => ({
  ...vi.importActual('lodash'),
  debounce: vi.fn((fn) => fn),
}))

describe('useExhibitionAndWeather store', () => {
  beforeEach(() => {
    setActivePinia(createPinia())
  })

  it('initializes with correct default values', () => {
    const store = useExhibitionAndWeather()

    expect(store.state.data).toBeNull()
    expect(store.state.searchText).toBe('')
    expect(store.state.page).toBe(0)
  })

  it('computes searchParams correctly', () => {
    const mockResponse = { data: { records: [{ id: 1, title: 'Exhibition 1' }] } }
    ;(getExhibitionAndWeather as vi.Mock).mockResolvedValue(mockResponse)
    const store = useExhibitionAndWeather()

    expect(store.state.searchParams).toEqual({})

    store.state.searchText = 'test'
    expect(store.state.searchParams).toEqual({ q: 'title:test' })

    store.state.page = 1
    expect(store.state.searchParams).toEqual({ q: 'title:test', page: '2' })
  })

  it('fetches data correctly on fetchData action', async () => {
    const store = useExhibitionAndWeather()
    const mockResponse = { data: { records: [{ id: 1, title: 'Exhibition 1' }] } }
    ;(getExhibitionAndWeather as vi.Mock).mockResolvedValue(mockResponse)

    await store.actions.fetchData()
    await flushPromises()

    expect(getExhibitionAndWeather).toHaveBeenCalledWith({})
    expect(store.state.data).toEqual(mockResponse.data)
  })

  it('appends data on subsequent fetches when page is greater than 0', async () => {
    const store = useExhibitionAndWeather()
    const initialResponse = { data: { records: [{ id: 1, title: 'Exhibition 1' }] } }
    const subsequentResponse = { data: { records: [{ id: 2, title: 'Exhibition 2' }] } }
    ;(getExhibitionAndWeather as vi.Mock).mockResolvedValueOnce(initialResponse)
    ;(getExhibitionAndWeather as vi.Mock).mockResolvedValueOnce(subsequentResponse)

    await store.actions.fetchData()
    await flushPromises()

    store.state.page = 1
    await flushPromises()

    expect(store.state.data).toEqual({
      records: [
        { id: 1, title: 'Exhibition 1' },
        { id: 2, title: 'Exhibition 2' },
      ],
    })
  })

  it('resets page to 0 and fetches data when searchText changes', async () => {
    const store = useExhibitionAndWeather()
    const mockResponse = { data: { records: [{ id: 1, title: 'Exhibition 1' }] } }
    ;(getExhibitionAndWeather as vi.Mock).mockResolvedValue(mockResponse)

    store.state.searchText = 'new search'
    await flushPromises()

    expect(store.state.page).toBe(0)
    expect(getExhibitionAndWeather).toHaveBeenCalledWith({ q: 'title:new search' })
    expect(store.state.data).toEqual(mockResponse.data)
  })
})
