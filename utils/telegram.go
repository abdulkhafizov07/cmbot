package utils

import (
	"bytes"
	"context"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"time"
)

type TelegramClient struct {
	Token  string
	Client *http.Client
}

func NewTelegramClient(token string) *TelegramClient {
	return &TelegramClient{
		Token: token,
		Client: &http.Client{
			Timeout: 5 * time.Second,
		},
	}
}

func (t *TelegramClient) Call(ctx context.Context, method string, payload any) ([]byte, error) {
	url := fmt.Sprintf("https://api.telegram.org/bot%s/%s", t.Token, method)

	var body io.Reader

	if payload != nil {
		b, err := json.Marshal(payload)
		if err != nil {
			return nil, err
		}
		body = bytes.NewBuffer(b)
	}

	req, err := http.NewRequestWithContext(ctx, http.MethodPost, url, body)
	if err != nil {
		return nil, err
	}

	req.Header.Set("Content-Type", "application/json")

	resp, err := t.Client.Do(req)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	return io.ReadAll(resp.Body)
}

func (t *TelegramClient) Reply(chatID int64, text string) {
	payload := map[string]any{
		"chat_id": chatID,
		"text":    text,
	}

	t.Call(context.Background(), "sendMessage", payload)
}
